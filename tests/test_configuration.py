import logging

import pytest
from pylot.configuration import Field, Configuration, ConfigurationError


logging.basicConfig(level=logging.INFO, format=' %(message)s')


class TestConfig(Configuration):
    foo = Field()


def test_simple_config():
    """Test that a Value can be set in a Configuration."""
    config = TestConfig(values={'foo': 'bar'})

    assert config.foo == 'bar'


def test_default_config():
    """Test that a default Value can be set in a Configuration."""
    class DefaultConfig(Configuration):
        # fields = {
        #     'foo': Field(),
        #     'bar': Field(default='BAR'),
        # }
        foo = Field()
        bar = Field(default='BAR')

    config = DefaultConfig(values={'foo': 'FOO'})

    assert config.foo == 'FOO'
    assert config.bar == 'BAR'


def test_not_required_if_default():
    """Test that a field is required if no default is specified."""
    with pytest.raises(ConfigurationError):
        TestConfig(values={})


def test_default_none():
    """Test that `None` is a valid default value.

    (We use a sentinel object to store "no-default").
    """
    class NoneDefaultConfig(Configuration):
        none = Field(default=None)

    config = NoneDefaultConfig(values={})

    assert config.none is None
