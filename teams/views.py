from rest_framework import  permissions, viewsets


from teams.models import Team
from users.serializers import TeamPlayerSerializer


class TeamPlayerViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TeamPlayerSerializer
    #permission_classes = [permissions.AllowAny]
    #filterset_fields = ['player__username']
    def get_queryset(self):
        return Team.objects.all()

# Create your views here.
