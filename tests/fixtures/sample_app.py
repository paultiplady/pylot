"""Sample working app configuration."""
from kubernetes.client import V1PodSpec, V1Container, V1Pod
from pylot.configuration import Configuration, Field


class SampleAppConfiguration(Configuration):
    foo = Field(default='FOO')
    bar = Field()


# TODO: How to register these pods?
# As currently implemented, we'll only collect API objects that are exported like this one.
# 1) Could define another aggregate for Specs / Ensemble / attach to Configuration.
# 2) Could add a decorator to manually register.
# 3) Could define subclasses for all of the API objects which register when instantiated.
pod = V1Pod(
    spec=V1PodSpec(
        containers=[
            V1Container(
                name='foo',
                command='bash -c "while date do; sleep 1; done',
                image='busybox',
            ),
        ],
    ),
)