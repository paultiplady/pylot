

# TODO: Naming: Call this something more expressive/less generic?
# Manifest?

import yaml
from kubernetes.client import ApiClient
from pylot.configuration import Field


class Job:
    def __init__(self, configuration_cls, objects):
        self.configuration_cls = configuration_cls
        self.objects = objects

    def render(self, values: dict):
        configuration = self.configuration_cls(values=values)

        for obj in self.objects:
            self._recursively_render_object(obj, configuration)

    @classmethod
    def _recursively_render_object(cls, obj, configuration):
        # We only care about typed Swagger objects, which all have a `.swagger_types` attr listing their sub-objects.
        for swagger_field_name in getattr(obj, 'swagger_types', []):
            # Fetch the object's version of the Field
            field_from_object = getattr(obj, swagger_field_name, None)

            if isinstance(field_from_object, Field):
                # Field instances are all primitive data types, so we don't need to recurse here.
                # Just replace the Field with the value derived from the configuration.
                setattr(obj, swagger_field_name, field_from_object.value)
            else:
                cls._recursively_render_object(field_from_object, configuration)

    def objects_to_yaml(self):
        client = ApiClient()

        return '\n---\n'.join(
            # Use a generator here to avoid building an intermediate list.
            yaml.dump(client.sanitize_for_serialization(obj)) for obj in self.objects
        )
