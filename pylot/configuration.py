import logging

_log = logging.getLogger(__name__)


class Field:
    NONE = object()

    def __init__(self, default=NONE):
        self.default = default


class ConfigurationMetaClass(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        _log.debug('Building Class %s.', name)
        klass = type.__new__(mcs, name, bases, namespace, **kwargs)

        klass.fields = {}

        for k, v in namespace.items():
            if isinstance(v, Field):
                _log.debug('Got Field %s.', k)
                # namespace.pop(k)
                klass.fields[k] = v

        return klass


class Configuration(metaclass=ConfigurationMetaClass):
    fields = None

    def __init__(self, values):
        for name, field in self.fields.items():
            if name in values:
                _log.debug('Field "%s" was provided in values: %s', name, values)
                value = values.pop(name)
                setattr(self, name, value)
            elif field.default is not Field.NONE:
                _log.debug('Field "%s" was defaulted: %s', name, field.default)
                setattr(self, name, field.default)
            else:
                raise ConfigurationError('Configuration field "%s" was not provided in values, '
                                         'and there is no default value.' % name)


class ConfigurationError(Exception):
    pass
