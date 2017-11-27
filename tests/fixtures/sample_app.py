"""Sample working app configuration."""
from kubernetes.client import V1PodSpec, V1Container, V1Pod, V1ObjectMeta
from pylot.configuration import Configuration, Field
from pylot.job import Job


class SampleAppConfiguration(Configuration):
    foo = Field(default='FOO')
    bar = Field()
    name = Field(default='THE NAME')


# TODO: How to register these pods?
# As currently implemented, we'll only collect API objects that are exported like this one.
# 1) Could define another aggregate for Specs / Ensemble / attach to Configuration.
# 2) Could add a decorator to manually register.
# 3) Could define subclasses for all of the API objects which register when instantiated.
pod = V1Pod(
    metadata=V1ObjectMeta(
        name=SampleAppConfiguration.name,
    ),
    spec=V1PodSpec(
        containers=[
            V1Container(
                name='container-foo',
                command=['sh', '-c', 'while date; do sleep 1; done'],
                image='busybox',
            ),
        ],
    ),
)


sample_job = Job(
    configuration_cls=SampleAppConfiguration,
    objects=[
        pod,
    ]
)

__all__ = [
    'sample_job',
]


"""
Can we write this?

class SampleJob(Job):
    configuration = SampleAppConfiguration
    # or even
    class Configuration(BaseConfiguration):
        ...
    
    specs = [
        V1Pod()
        V1Pod()
    ]
    # or even
    V1Pod()
    
job = SampleJob(values=values)
"""
