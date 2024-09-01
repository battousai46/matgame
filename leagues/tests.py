from leagues.factories import UserFactory, LeagueFactory
from django.test import TestCase

class ViewTests(TestCase):
    def setUp(self):
        # Authenticate client
        self.user = UserFactory()
        self.league = LeagueFactory()

    def test_league_serializer(self):
        from leagues.serializers import LeagueSerializer
        serialized_data = LeagueSerializer(self.league).data
        assert list(serialized_data.keys()) == ['id','title','team']
        from users.serializers import PlayerSerializer
        serialized_data = PlayerSerializer(self.user).data
        assert list(serialized_data.keys()) == ['pkid','username','email']


