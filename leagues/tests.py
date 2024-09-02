from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from http import HTTPStatus
from django.test import TestCase

from leagues.factories import UserFactory, LeagueFactory
from leagues.serializers import LeagueSerializer

from django.urls import reverse


from users.serializers import PlayerSerializer, MatGameTokenObtainSerializer

User = get_user_model()


class ViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.league = LeagueFactory()
        self.client = APIClient()

    def test_league_serializer(self):
        serialized_data = LeagueSerializer(self.league).data
        assert list(serialized_data.keys()) == ['id', 'title', 'team']

    def test_user_serializer(self):
        serialized_data = PlayerSerializer(self.user).data
        assert list(serialized_data.keys()) == ['pkid', 'username', 'email']

    def test_jwt_authorization_fail(self):
        self.user.type = User.Types.PLAYER
        self.refresh = MatGameTokenObtainSerializer.get_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh.access_token}")
        self.client.force_authenticate(user=self.user)
        expected_error_data = "Access requires permission of LEAGUE ADMIN, staff or admin users"
        response = self.client.get(reverse("league-list"), format="json")
        assert response.data.get("detail") == expected_error_data
        assert response.status_code == HTTPStatus.FORBIDDEN

    def test_jwt_authorization_pass(self):
        self.user.type = User.Types.LEAGUE_ADMIN
        self.refresh = MatGameTokenObtainSerializer.get_token(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.refresh.access_token}")
        response = self.client.get(reverse("league-list"), format="json")
        assert response.status_code == HTTPStatus.OK
