from kubernetes.client.models import V1Pod


class Pod(V1Pod):
    pass


__exports__ = ('Pod',)
