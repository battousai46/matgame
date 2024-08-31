from rest_framework.routers import DefaultRouter
from leagues.views import LeagueViewSet

urlpatterns = []

router = DefaultRouter()
router.register("league", LeagueViewSet, basename="league")

urlpatterns += router.urls
