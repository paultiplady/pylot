import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format='%(message)s')


class PylotError(Exception):
    pass
