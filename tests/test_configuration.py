from pylot.configuration import Value, Configuration


def test_simple_config():
    class TestConfig(Configuration):
        foo = Value()

    config = TestConfig(values={'foo': 'bar'})

    assert config.foo == 'bar'
