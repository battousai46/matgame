from django.db import models

from users.models import PlayerDetails

""""
Each round of a league tournament consist of games
games contain two participants of team, one of them is winner
winning team scores , and each participant player of that winning team also scores
participation count for both team increases
"""

from teams.models import Team

class Game(models.Model):
    """
      Game represents an elimination round between two team
      it also updates the corresponding team and individual participants scores and attrs
    """
    losing_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='losing_team')
    winning_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winning_team')

    def update_individual_player_score(self):
        # this bulk update should be asyncronous, can be awaited as courotine or defered by celery tasks
        losing_players = self.losing_team.players.all()
        # increase losing team player participation
        for ith_player in losing_players:
            ith_player.increase_participation()

        # this block is partially repetitive as above, can refactored to same method
        winning_players = self.winning_team.players.all()
        for ith_player in winning_players:
            ith_player.increase_participation()
            ith_player.increase_wins()





    def save(self, *args, **kwargs) -> None:
        # update winning score and losing team participation count
        """"
           winning and losing is part of the game / elemination round
           this method should bulk update dependant attributes then save the record
        """
        self.losing_team.increase_participation()

        self.winning_team.increase_participation()
        self.winning_team.increase_wins()

        self.update_individual_player_score()

        super().save(*args, **kwargs)
