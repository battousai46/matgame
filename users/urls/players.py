from rest_framework.routers import DefaultRouter

urlpatterns = []
router = DefaultRouter()
from users.views import PlayerDetailsViewSet
router.register("player", PlayerDetailsViewSet, basename="player")
urlpatterns += router.urls






