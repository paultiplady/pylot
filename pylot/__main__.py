"""Pylot is a tool for interacting with Kubernetes in a Pythonic way.

Usage:
    pylot dump MODULE
    pylot deploy MODULE [--dry-run] [--debug]

"""
import importlib
import logging

from docopt import docopt
from kubernetes.client import V1Pod

_log = logging.getLogger(__name__)


def main():
    logging.basicConfig(level=logging.INFO, format=' %(message)s')

    args = docopt(__doc__)
    if 'dump' in args:
        dump(args)
    elif 'deploy' in args:
        deploy(args)


def dump(args):
    _log.setLevel(logging.DEBUG)
    module_ = args['MODULE']

    _log.debug('Dumping %s', module_)

    imported = importlib.import_module(module_)
    _log.debug('Imported: %s', imported)
    for reference, obj in imported.__dict__.items():
        if type(obj) in (V1Pod,):
            _log.debug('Got instance: %s', reference)


def deploy(args):
    module_ = args['MODULE']
    dry_run = args['--dry-run']
    debug = args['--debug']

    if debug:
        _log.setLevel(logging.DEBUG)


if __name__ == '__main__':
    main()
