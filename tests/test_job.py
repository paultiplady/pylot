from kubernetes.client import V1Pod, V1ObjectMeta, V1PodSpec, V1Container
from pylot.configuration import Field, Configuration
from pylot.job import Job
from tests.fixtures.complex_app import complex_job


class SimpleConfiguration(Configuration):
    name = Field(default='THE NAME')


simple_job = Job(
    configuration_cls=SimpleConfiguration,
    objects=[
        V1Pod(
            metadata=V1ObjectMeta(
                name=SimpleConfiguration.name,
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
        ),
    ]
)


def test_simple_job():
    """Test that a Configuration and Spec list can be combined to get a deployable Job."""
    simple_job.render(values={'bar': 'BAR', 'name': 'MY NAME'})

    assert simple_job.objects
    assert simple_job.objects[0].metadata.name == 'MY NAME'


def test_job_to_yaml():
    """Test that a Configuration and Spec list can be combined to get a deployable Job."""
    simple_job.render(values={'bar': 'BAR', 'name': 'MY NAME'})

    assert simple_job.objects_to_yaml() == """metadata: {name: MY NAME}
spec:
  containers:
  - command: [sh, -c, while date; do sleep 1; done]
    image: busybox
    name: container-foo
"""


def test_complex_job():
    """Test that a job with multiple specs can be configured correctly."""
    complex_job.render(values={'name': 'COMPLEX NAME', 'service_name': 'SERVICE NAME'})

    assert complex_job.objects[0].metadata.name == 'COMPLEX NAME'
    assert complex_job.objects[1].metadata.name == 'SERVICE NAME'
