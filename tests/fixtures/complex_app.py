from kubernetes.client import V1ObjectMeta, V1PodSpec, V1Container, V1Service
from kubernetes.client.models.apps_v1beta1_deployment import AppsV1beta1Deployment
from kubernetes.client.models.apps_v1beta1_deployment_spec import AppsV1beta1DeploymentSpec
from kubernetes.client.models.v1_pod_template_spec import V1PodTemplateSpec
from kubernetes.client.models.v1_service_spec import V1ServiceSpec
from pylot.configuration import Configuration, Field
from pylot.job import Job


class AppConfiguration(Configuration):
    name = Field(default='THE NAME')
    service_name = Field(default='THE SERVICE NAME')


complex_job = Job(
    configuration_cls=AppConfiguration,
    objects=[
        AppsV1beta1Deployment(
            metadata=V1ObjectMeta(
                name=AppConfiguration.name,
            ),
            spec=AppsV1beta1DeploymentSpec(
                replicas=2,
                template=V1PodTemplateSpec(
                    metadata=V1ObjectMeta(
                        name='pod-name',
                        labels={
                            'app': 'foo-app',
                        },
                    ),
                    spec=V1PodSpec(
                        containers=[
                            V1Container(
                                name='container-name',
                                command=['sh', '-c', 'while date; do sleep 1; done'],
                                image='busybox',
                            ),
                        ],
                    ),
                ),
            ),
        ),
        V1Service(
            metadata=V1ObjectMeta(
                name=AppConfiguration.service_name,
            ),
            spec=V1ServiceSpec(
                selector={'app': 'foo-app'}
            )
        )
    ]
)
