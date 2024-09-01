from cgi import print_environ_usage

from rest_framework import serializers
from leagues.models import League, Round
from teams.serializers import TeamsSerializer
from games.serializers import GameSerializer

class LeagueSerializer(serializers.ModelSerializer):
    team = TeamsSerializer(many=True, read_only=True)

    class Meta:
        model = League
        fields = [
            "id",
            "title",
            "team"
        ]


class RoundSerializer(serializers.ModelSerializer):
    round_number = serializers.IntegerField(read_only=True)
    # each round have participants / 2 matches
    match_number = serializers.IntegerField(read_only=True)
    league_title = serializers.CharField(source='league.title')
    game = GameSerializer(read_only=True)

    class Meta:
        model = Round
        fields = [
            "id",
            "round_number",
            "match_number",
            "league_title",
            "game"
        ]



