from rest_framework import serializers

from teams.models import Team


# TODO hyper link to player details model view
class TeamsSerializer(serializers.HyperlinkedModelSerializer):
    name = serializers.PrimaryKeyRelatedField(read_only=True)
    coach = serializers.SerializerMethodField()
    team_participation = serializers.IntegerField(read_only=True)
    team_wins = serializers.IntegerField(read_only=True)

    class Meta:
        model = Team
        fields = [
            "id",
            "name",
            "coach",
            "team_participation",
            "team_wins"
        ]

    def get_coach(self, obj) -> str | None:
        if obj.coach:
            return obj.coach.username
        return None
