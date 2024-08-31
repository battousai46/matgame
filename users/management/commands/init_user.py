from django.core.management.base import BaseCommand, CommandError

from ...models import Player, Coach, LeagueAdminManager, PlayerDetails, User


class Command(BaseCommand):
    help = "Adds a few base users"

    def handle(self, *args, **options):
        User.objects.all().delete()
        p = Player.objects.create(
            username="irfan", email="irfan@test.com", is_superuser=True, type=User.Types.PLAYER
        )
        PlayerDetails.objects.create(user=p, total_participation=2, total_wins=1);
        self.stdout.write(self.style.SUCCESS("irfan player initiated"))
