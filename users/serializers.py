from rest_framework import serializers

from teams.serializers import TeamsSerializer
from users.models import Coach, Player, PlayerDetails
from teams.models import Team

"""
   respective custom type user serializers and logic can be refactored to specific modules thus apps  
"""


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
        fields = ['pkid', 'username', 'email']


class TeamPlayerSerializer(serializers.ModelSerializer):
    player = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ["id",
                  "name",
                  "coach",
                  "team_participation",
                  "team_wins",
                  'player'
                  ]

    def get_player(self, obj):
        if obj.players:
            team_players = PlayerDetailsSerializer(obj.players.all(), many=True).data
            return team_players
        return None


class PlayerDetailsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    team = serializers.SerializerMethodField()

    class Meta:
        model = PlayerDetails
        fields = ['individual_participation', 'individual_wins', 'user', 'team']

    def get_user(self, obj) -> str | None:
        if obj.user:
            return PlayerSerializer(obj.user).data
        return None

    def get_team(self, obj) -> str | None:
        if obj.team:
            return TeamsSerializer(obj.team).data
        return None
