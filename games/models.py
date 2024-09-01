from django.db import models

""""
Each round of a league tournament consist of games
games contain two participants of team, one of them is winner
winning team scores , and each participant player of that winning team also scores
participation count for both team increases
"""

from teams.models import Team

class Game(models.Model):
    losing_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='losing_team')
    winning_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winning_team')
    def save(self, *args, **kwargs) -> None:
        # TODO update participant player winning score
        # update winning score and losing team participation count
        super().save(*args, **kwargs)
