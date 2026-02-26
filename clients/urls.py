from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('featured-works', FeaturedWorksViewSet)
router.register('review', ReviewViewSet)

urlpatterns = router.urls