from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from rest_envelope.decorators import envelope
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


class TestViewSetWithDecorator(GenericViewSet):
    @envelope("baz")
    def list(self, request: Request, *args, **kwargs) -> Response:
        return Response([{"foo": "bar"}])
