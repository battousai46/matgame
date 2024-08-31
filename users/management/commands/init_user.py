from django.core.management.base import BaseCommand, CommandError

from ...models import Player, Coach, LeagueAdminManager, PlayerDetails, User
from teams.models import Team


class Command(BaseCommand):
    help = "Adds a few base users"

    def handle(self, *args, **options):
        #User.objects.all().delete() #do this for cleanup if needed
        #Team.objects.all().delete()
        c = Coach.objects.get_or_create(username='test_coach', email="test@c.com",type=User.Types.COACH)
        p1 = Player.objects.get_or_create(
            username="irfan", email="irfan@test.com", is_superuser=True, type=User.Types.PLAYER
        )
        p2 = Player.objects.get_or_create(
            username="nabil", email="nabil@test.com", is_superuser=True, type=User.Types.PLAYER
        )
        team  = Team.objects.filter(name__iexact="test_team")
        if not team.exists():
            team = Team.objects.create(name="test_team",coach=c[0])
        else:
            team = team.first()

        PlayerDetails.objects.get_or_create(user=p1[0], total_participation=2, total_wins=1, team=team);
        PlayerDetails.objects.get_or_create(user=p2[0], total_participation=2, total_wins=1, team=team);

        all_players = team.players.all()
        print(all_players)
        self.stdout.write(self.style.SUCCESS("irfan, nabil players are initiated"))


