from rest_framework.routers import DefaultRouter
from leagues.views import LeagueViewSet, RoundViewSet

urlpatterns = []

router = DefaultRouter()
router.register("league", LeagueViewSet, basename="league")
router.register( "round", RoundViewSet, basename="round")

urlpatterns += router.urls
