import logging
from pprint import pformat

import yaml
from pylot.loader import import_

_log = logging.getLogger(__name__)


def dump(args):
    _log.setLevel(logging.DEBUG)
    module_ = args['MODULE']

    _log.debug('Dumping %s', module_)

    import_(module_)


class CommandError(Exception):
    pass


def deploy(args):
    module_ = args['MODULE']
    dry_run = args['--dry-run']
    debug = args['--debug']

    if debug:
        _log.setLevel(logging.DEBUG)

    specs, configuration_cls = import_(module_)

    values_path = args['VALUES_FILE']
    if values_path:
        values = yaml.load(values_path)
    else:
        values = {}

    _log.warning('Got configuration: %s', pformat(values))

    configuration = configuration_cls(values=values)


