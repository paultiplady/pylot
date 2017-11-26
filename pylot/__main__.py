"""Pylot is a tool for interacting with Kubernetes in a Pythonic way.

Usage:
    pylot dump MODULE
    pylot deploy MODULE [--dry-run] [--debug] [--values=VALUES_FILE]

"""
import logging

import sys
from docopt import docopt
from pylot import commands, PylotError

_log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format=' %(message)s')


def main():
    args = docopt(__doc__)

    try:
        if args['dump']:
            commands.dump(args)
        elif args['deploy']:
            commands.deploy(
                module_=args['MODULE'],
                dry_run=args['--dry-run'],
                debug=args['--debug'],
                values_path=args['--values'],
            )
    except PylotError as e:
        print('ERROR: %s' % e, file=sys.stderr)


if __name__ == '__main__':
    main()
