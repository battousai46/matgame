from django.db import models


from users.models import User


class Team(models.Model):
    name = models.CharField(unique=True,max_length=100)
    coach = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="team")
    team_participation = models.IntegerField(default=0)
    team_wins = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs) -> None:
        if self.coach and not self.coach.type == User.Types.COACH:
            raise ValueError(
                "Only coach can manage a team"
            )
        super().save(*args, **kwargs)

    def get_average_rating(self):
        average = 0
        if self.team_participation:
            average = self.team_wins / self.team_participation
        return average if average is not None else 0.0

