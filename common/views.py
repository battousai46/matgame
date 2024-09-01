from django.contrib.auth import get_user_model
from rest_framework import  permissions
User = get_user_model()

class IsLeagueAdminOrStaffOrSuperUser(permissions.BasePermission):
    def __init__(self) -> None:
        self.message = None

    def has_permission(self, request, view):
        is_authorized = (
            request.user
            and request.user.is_authenticated
            and (request.user.is_staff or request.user.is_superuser
                 or request.user.type == User.Types.LEAGUE_ADMIN))
        if not is_authorized:
            self.message = (
                f"Access requires permission of {User.Types.LEAGUE_ADMIN}, staff or admin users"
            )
        return is_authorized


class IsCoach(permissions.BasePermission):
    def __init__(self) -> None:
        self.message = None

    def has_permission(self, request, view):
        is_authorized = (
            request.user
            and request.user.is_authenticated
            and request.user.type == User.Types.COACH)
        if not is_authorized:
            self.message = (
                f"Access requires permission of {User.Types.COACH} users"
            )
        return is_authorized


class IsPlayer(permissions.BasePermission):
    def __init__(self) -> None:
        self.message = None

    def has_permission(self, request, view):
        is_authorized = (
            request.user
            and request.user.is_authenticated
            and request.user.type == User.Types.PLAYER)
        if not is_authorized:
            self.message = (
                f"Access requires permission of {User.Types.PLAYER} users"
            )
        return is_authorized
