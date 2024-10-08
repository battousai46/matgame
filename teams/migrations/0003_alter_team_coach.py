# Generated by Django 4.2.15 on 2024-09-01 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("teams", "0002_alter_team_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="coach",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="team",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
