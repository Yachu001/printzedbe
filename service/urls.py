from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('core-service', CoreServiceViewSet)
router.register('we-provide', WeProvideViewSet)


urlpatterns = router.urls