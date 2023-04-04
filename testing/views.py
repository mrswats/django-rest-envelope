from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_envelope.mixins import ListEnvelopeMixin
from testing.models import TestModel
from testing.serializers import TestSerializer


class BaseClass(ReadOnlyModelViewSet):
    queryset = TestModel.objects.all()
    serializer_class = TestSerializer


class TestViewSetNoEnvelope(ListEnvelopeMixin, BaseClass):
    pass


class TestViewSet(ListEnvelopeMixin, BaseClass):
    envelope = "tests"
