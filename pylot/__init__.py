import logging

logging.basicConfig(level=logging.DEBUG, format=' %(message)s')
log = logging.getLogger(__name__)


class PylotError(Exception):
    pass