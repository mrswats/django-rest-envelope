from rest_framework.routers import SimpleRouter

from testing.views import TestViewSet
from testing.views import TestViewSetNoEnvelope
from testing.views import TestViewSetWithDecorator

router = SimpleRouter()
router.register("test-ok", TestViewSet, basename="test-ok")
router.register("test-err", TestViewSetNoEnvelope, basename="test-error")
router.register("test-decorator", TestViewSetWithDecorator, basename="test-decorator")

urlpatterns = router.urls
