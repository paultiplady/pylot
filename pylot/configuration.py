import logging

_log = logging.getLogger(__name__)


class Value:
    pass


class Configuration:
    fields = {}

    def __init__(self, values):
        for name, value in values.items():
            setattr(self, name, value)
