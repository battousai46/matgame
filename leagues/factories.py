from django.contrib.auth import get_user_model
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory import post_generation
from factory.fuzzy import FuzzyInteger
from factory.fuzzy import FuzzyText
from leagues.models import League
from leagues.models import Team

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = FuzzyText(length=10)
    password = FuzzyText(length=10)
    type = User.Types.LEAGUE_ADMIN


class TeamFactory(DjangoModelFactory):
    class Meta:
        model = Team

    name = FuzzyText(length=100)
    coach = SubFactory(UserFactory)
    team_participation = FuzzyInteger(1, 40)
    team_wins = FuzzyInteger(1, 40)


class LeagueFactory(DjangoModelFactory):
    class Meta:
        model = League

    title = FuzzyText(length=100)

    @post_generation
    def team(self, create, extracted):
        if not create:
            return
        if extracted:
            for ith in extracted:
                self.team.add(ith)

