from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('marketing-solutions', MarketingSolutionsViewSet)
router.register('portfolio', PortfolioViewSet)
router.register('team-members', TeamMemberViewSet)


urlpatterns = router.urls