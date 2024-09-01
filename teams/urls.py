from rest_framework.routers import DefaultRouter

urlpatterns = []
router = DefaultRouter()
from teams.views import TeamPlayerViewSet
router.register("team", TeamPlayerViewSet, basename="team")
urlpatterns += router.urls
