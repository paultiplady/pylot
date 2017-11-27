import logging
from pprint import pformat

import kubernetes
import yaml
from pylot import log, PylotError
from pylot.job import Job
from pylot.loader import import_
from tests.fixtures import all_default_app


def dump(args):
    log.setLevel(logging.DEBUG)
    module_ = args['MODULE']

    log.debug('Dumping %s', module_)

    import_(module_)


class CommandError(PylotError):
    pass


def deploy(module_, values_path=None, dry_run=False, debug=False):
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)

    specs, configuration_cls = import_(module_)

    if values_path:
        values = yaml.load(values_path)
    else:
        values = {}

    log.debug('Got configuration: %s', pformat(values))

    job = Job(objects=specs, configuration_cls=configuration_cls)
    # configuration = configuration_cls(values=values)
    job.render(values)

    if dry_run:
        # print('Configuration:\n%s' % configuration)
        # print('Specs:\n%s' % specs)

        print(job.objects_to_yaml())
    else:
        print('Deploying...')
        # TODO: Fix this dummy implementation. This was added for exploratory purposes.
        kubernetes.config.load_kube_config()

        v1_client = kubernetes.client.CoreV1Api()

        pods = job.objects
        # pod = all_default_app.pod
        for pod in pods:
            create_response = v1_client.create_namespaced_pod(namespace='default', body=pod)
            log.debug('Response: %s', create_response)
