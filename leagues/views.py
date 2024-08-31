from django.shortcuts import render
from rest_framework import  generics, permissions, status
from rest_framework.views import  APIView
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from leagues.models import League
from leagues.serializers import LeagueSerializer


# Create your views here.

class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LeagueSerializer
    permission_classes = [permissions.AllowAny]
    #filter_backends = [DjangoFilterBackend]
    #filterset_fields = ["names"]

    def get_queryset(self):
        return League.objects.all()