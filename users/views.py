from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenViewBase

from rest_framework import permissions, viewsets
from users.models import Coach, PlayerDetails
from users.serializers import CoachSerializer, PlayerDetailsSerializer, MatGameTokenObtainSerializer

User = get_user_model()


class CoachViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CoachSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['username']

    def get_queryset(self):
        return Coach.objects.all()


class PlayerDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlayerDetailsSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['user__username']

    def get_queryset(self):
        return PlayerDetails.objects.all()


class MatGameTokenObtainPairView(TokenViewBase):
    serializer_class = MatGameTokenObtainSerializer
