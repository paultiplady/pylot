"""Sample app configuration that should fail to load, since there are multiple Configurations."""
from pylot.configuration import Configuration, Field


class SampleAppConfiguration(Configuration):
    foo = Field(default='FOO')
    bar = Field()


class SecondAppConfiguration(Configuration):
    bad = Field()
