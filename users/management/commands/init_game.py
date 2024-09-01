from random import randrange

from django.core.management.base import BaseCommand, CommandError

from ...models import Player, Coach, LeagueAdminManager, PlayerDetails, User
from teams.models import Team
from leagues.models import League, Round
from games.models import Game
from math import log2


class Command(BaseCommand):
    help = "initiate a new league of games 2^N teams"
    total_teams = 0
    def generate_players(self, team: Team):
        # generate or select 5 active player for each team
        # alternatively can choose randomly 5 players from each team
        for ith in range(1, 6):
            p = Player.objects.get_or_create(
                username="p_"+team.name+ str(ith), email="p" + str(ith) + "@t.com", is_superuser=True, type=User.Types.PLAYER
            )
            #postgres nextval sequential id lock may raise duplicate key error
            #pd = PlayerDetails.objects.get_or_create(user=p[0], team=team)
            try:
                pd_ = PlayerDetails.objects.get(user=p[0], team=team)
            except PlayerDetails.DoesNotExist:
                pd_ = PlayerDetails(user=p[0], team=team)
                pd_.save()


    def generate_logN_rounds(self, teams: list, league: League, round_no: int):
        # from 2^N teams, process logN rounds
        if(round_no > log2(Command.total_teams)):
            print("--------GAME OVER--------")
            return
        total_team = len(teams)
        team_a = randrange(total_team)
        team_b = randrange(total_team)
        already_played = dict();
        ith_match = 1
        next_teams = []
        while len(already_played.keys()) != total_team:
            while already_played.get(team_a):
                team_a = randrange(total_team)
            already_played[team_a] = True
            while already_played.get(team_b):
                team_b = randrange(total_team)
            already_played[team_b] = True
            game = Game.objects.get_or_create(losing_team=teams[team_a], winning_team=teams[team_b])
            round_ = Round.objects.get_or_create(round_number=round_no, match_number=ith_match, game=game[0], league=league)
            print(f"-------round {round} match {ith_match}   {team_a}  vs  {team_b} -->  {teams[team_a]} lost to {teams[team_b]} ")

            # only winning team proceeds
            next_teams.append(teams[team_b])
            ith_match += 1
        print("----------------NEXT ROUND--------------")
        self.generate_logN_rounds(next_teams, league, round_no+1)

    def generate_team_assign_coach(self, league_title: str):
        # create 2^N teams / for test purpose create 8 teams
        print(f"generating teams for {league_title}")
        league = League(title=league_title)
        league.save()
        teams = []
        Command.total_teams = int(pow(2, log2( 16 )))
        for ith in range(Command.total_teams):
            team_name = "go8_team_" + str(ith + 1)
            coach = Coach.objects.get_or_create(username="coach" + str(ith), email="t" + str(ith) + "@c.com",
                                                type=User.Types.COACH)
            team = Team.objects.filter(name__iexact=team_name)
            if not team.exists():
                team = Team.objects.create(name=team_name, coach=coach[0])
            else:
                team = team.first()
            self.generate_players(team)
            league.team.add(team)
            league.save()
            teams.append(team)
        self.generate_logN_rounds(teams, league, 1)


    def print_league_summary(self, league_title: str):
        league = League.objects.get(title=league_title)
        all_matches = league.matches.all()
        for match in all_matches:
            print(f"-------------#ROUND {match.round_number}  SUMMARY:---------")
            game = match.game
            print(f"{game.losing_team.name} vs {game.winning_team.name}")
            print("winning team players:")
            print(game.winning_team.players.all())
            print("********--------------NEXT--------------********")

    def clear_all_db(self):
        User.objects.all().delete()
        Team.objects.all().delete()
        Game.objects.all().delete()
        Player.objects.all().delete()
        Round.objects.all().delete()
        League.objects.all().delete()
        PlayerDetails.objects.all().delete()
        Round.objects.all().delete()


    def handle(self, *args, **options):
        "start a league of games 2^N teams and logN rounds of eliminating games"

        #clean if needed
        self.clear_all_db()

        league_title = "GameOf16PowerOf2"

        self.generate_team_assign_coach(league_title)

        self.print_league_summary(league_title)

        self.stdout.write(self.style.SUCCESS("irfan, nabil players are initiated"))
