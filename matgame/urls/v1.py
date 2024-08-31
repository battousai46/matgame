from django.urls import include
from django.urls import path

urlpatterns = [
    path("leagues/", include("leagues.urls")),
]
