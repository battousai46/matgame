from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class LeaguesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "leagues"
    verbose_name = _("Leagues")
