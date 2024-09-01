from rest_framework import serializers

from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    losing_team = serializers.CharField(source='losing_team.name', read_only=True)
    winning_team = serializers.CharField(source='winning_team.name', read_only=True)

    class Meta:
        model = Game
        fields = [
            "id",
            "losing_team",
            "winning_team",
        ]

