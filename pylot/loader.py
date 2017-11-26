import importlib
from typing import List, Type

from kubernetes.client import V1Pod
from pylot import log, PylotError
from pylot.configuration import Configuration


def import_(module_: str) -> (List, Type[Configuration]):
    imported = importlib.import_module(module_)
    log.debug('Imported: %s', imported)

    specs = []
    configuration = None
    for reference, obj in imported.__dict__.items():
        if type(obj) in (V1Pod,):
            log.debug('Got instance: %s', reference)
            specs.append(obj)
        elif isinstance(obj, type) and obj is not Configuration and issubclass(obj, Configuration):
            log.debug('Got configuration: %s', obj)
            # Check we didn't find a Configuration already.
            if configuration:
                raise LoaderError('Found multiple Configurations: %s, %s. '
                                  'May only have one Configuration in the module %s.' %
                                  (obj, configuration, module_))
            else:
                configuration = obj

    return specs, configuration


class LoaderError(PylotError):
    pass
