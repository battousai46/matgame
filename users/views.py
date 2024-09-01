from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView,
)
from rest_framework import  permissions, viewsets
from users.models import Coach, PlayerDetails
from users.serializers import CoachSerializer, PlayerDetailsSerializer

User = get_user_model()


class CoachViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CoachSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['username']
    def get_queryset(self):
        return Coach.objects.all()

class PlayerDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = PlayerDetailsSerializer
    permission_classes = [permissions.AllowAny]
    filterset_fields = ['user__username']
    def get_queryset(self):
        return PlayerDetails.objects.all()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, UpdateView):
    fields = [
        "name",
    ]

    model = User

    def get_success_url(self):
        return reverse(
            "users:detail",
            kwargs={'username': self.request.user.username},
        )

    def get_object(self):
        return User.objects.get(
            username=self.request.user.username
        )


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse(
            "users:detail",
            kwargs={"username": self.request.user.username},
        )


user_redirect_view = UserRedirectView.as_view()