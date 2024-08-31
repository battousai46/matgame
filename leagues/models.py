from django.db import models
from games.models import Game
from teams.models import Team

"""
   Each league can form with 2^N teams
   and in each of the log( 2^N ) elimination round, two team participates in a game
"""


class League(models.Model):
    title = models.CharField(unique=True, max_length=100)
    team = models.ManyToManyField(Team, related_name='leagues')


class Round(models.Model):
    class Meta:
        unique_together = ("round_number","match_number", "game")

    # 1 2 upto log(2^N) games
    round_number = models.IntegerField()
    # each round have participants / 2 matches
    match_number = models.IntegerField(default=0)
    game = models.OneToOneField(Game, on_delete=models.CASCADE, related_name='round')
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='matches')
