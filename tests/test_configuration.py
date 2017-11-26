import logging

import pytest
from pylot.configuration import Field, Configuration, ConfigurationError


logging.basicConfig(level=logging.INFO, format=' %(message)s')


class SimpleConfig(Configuration):
    foo = Field()


class DefaultConfig(Configuration):
    foo = Field()
    bar = Field(default='BAR')


def test_simple_config():
    """Test that a Value can be set in a Configuration."""
    config = SimpleConfig(values={'foo': 'bar'})

    assert config.foo == 'bar'


def test_default_config():
    """Test that a default Value can be set in a Configuration."""
    config = DefaultConfig(values={'foo': 'FOO'})

    assert config.foo == 'FOO'
    assert config.bar == 'BAR'


def test_not_required_if_default():
    """Test that a field is required if no default is specified."""
    with pytest.raises(ConfigurationError):
        SimpleConfig(values={})


def test_default_none():
    """Test that `None` is a valid default value.

    (We use a sentinel object to store "no-default").
    """
    class NoneDefaultConfig(Configuration):
        none = Field(default=None)

    config = NoneDefaultConfig(values={})

    assert config.none is None


def test_configuration_str():
    """Test that a simple string representation can be rendered for a Configuration instance."""
    config = DefaultConfig(values={'foo': 'FOO!'})
    assert str(config) == str({'foo': 'FOO!', 'bar': 'BAR'})
