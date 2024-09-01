from django.urls import include
from django.urls import path

urlpatterns = [
    path("leagues/", include("leagues.urls")),
    path("coaches/", include("users.urls.coaches")),
    path("players/", include("users.urls.players")),
    path("teams/", include("teams.urls")),
]
