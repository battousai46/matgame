from rest_framework.routers import DefaultRouter

urlpatterns = []
router = DefaultRouter()
from users.views import CoachViewSet
router.register("coach", CoachViewSet, basename="coach")
urlpatterns += router.urls
