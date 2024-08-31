import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    class Types(models.TextChoices):
        PLAYER = "PLAYER", "Player"
        COACH = "COACH", "Coach"
        LEAGUE_ADMIN = "LEAGUE ADMIN", "LeagueAdmin"

    base_type = Types.PLAYER

    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class PlayerManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.PLAYER)


class CoachManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.COACH)

class LeagueAdminManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.LEAGUE_ADMIN)


class PlayerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    total_participation = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)
    # TODO active players of a team limit is 5
    team = models.ForeignKey("teams.Team", on_delete=models.CASCADE, related_name="players", blank=True, null=True)
    def __str__(self):
        return self.user.username


class Player(User):
    base_type = User.Types.PLAYER
    objects = PlayerManager()
    @property
    def details(self):
        return self.playerdetails

    class Meta:
        proxy = True


class Coach(User):
    base_type = User.Types.COACH
    objects = CoachManager()

    @property
    def details(self):
        return self.playerdetails

    class Meta:
        proxy = True


