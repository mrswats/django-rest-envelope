from rest_framework.routers import SimpleRouter

from testing.views import TestViewSet
from testing.views import TestViewSetNoEnvelope

router = SimpleRouter()
router.register("test-ok", TestViewSet, basename="test-ok")
router.register("test-err", TestViewSetNoEnvelope, basename="test-error")

urlpatterns = router.urls
