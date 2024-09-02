from django.contrib.auth import get_user_model
from rest_framework import  permissions
from rest_framework import viewsets

from common.views import IsLeagueAdminOrStaffOrSuperUser
from leagues.models import League, Round
from leagues.serializers import LeagueSerializer, RoundSerializer

User = get_user_model()

# Create your views here.

class LeagueViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LeagueSerializer
    #permission_classes = [permissions.AllowAny]
    permission_classes = [IsLeagueAdminOrStaffOrSuperUser]
    filterset_fields = ['title']
    def get_queryset(self):
        return League.objects.all()


# rounds of a league could itself be another app if further enhancement requires
class RoundViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = RoundSerializer
    #filter_class and attributes when custom filtration required on rounds of a league
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['league__title']
    def get_queryset(self):
        return Round.objects.all()

