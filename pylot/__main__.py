"""Pylot is a tool for interacting with Kubernetes in a Pythonic way.

Usage:
    pylot dump MODULE
    pylot deploy MODULE [--dry-run] [--debug]

"""
import logging

from docopt import docopt
from pylot import commands

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=' %(message)s')


def main():
    args = docopt(__doc__)
    if 'dump' in args:
        commands.dump(args)
    elif 'deploy' in args:
        commands.deploy(args)


if __name__ == '__main__':
    main()
