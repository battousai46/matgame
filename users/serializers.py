from rest_framework import serializers

from teams.serializers import TeamsSerializer
from users.models import Coach, Player, PlayerDetails


class CoachSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)
    team = TeamsSerializer(read_only=True)

    class Meta:
        model = Coach
        fields = ['email', 'username', 'team']


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['pkid','username','email']


class PlayerDetailsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = PlayerDetails
        fields = ['total_participation','total_wins', 'user', 'team']

    def get_user(self, obj) -> str | None:
        if obj.user:
            return PlayerSerializer(obj.user).data
        return None

    def get_team(self, obj) -> str | None:
        if obj.team:
            return TeamsSerializer(obj.team).data
        return None



