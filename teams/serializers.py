from rest_framework import serializers

from teams.models import Team


class TeamsSerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(read_only=True)
    coach = serializers.SerializerMethodField()
    total_participation = serializers.IntegerField(read_only=True)
    total_wins = serializers.IntegerField(read_only=True)

    class Meta:
        model = Team
        fields = [
            "id",
            "name",
            "coach",
            "total_participation",
            "total_wins"
        ]

    def get_coach(self, obj):
        if obj.coach:
            return obj.coach.username
        return None
