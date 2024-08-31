from django.contrib.auth import get_user_model, forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


from django import forms as d_forms
from allauth.account.forms import SignupForm

User = get_user_model()


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(forms.UserCreationForm):
    error_message = forms.UserCreationForm.error_messages.update(
        {
            "duplicate_username": _(
                "This username has already been taken."
            )
        }
    )

    class Meta(forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(
            self.error_messages["duplicate_username"]
        )


class MatGameSignupForm(SignupForm):
    # Specify a choice field that matches the choice field on our user model
    type = d_forms.ChoiceField(choices=[
        ("PLAYER", "Player"),
        ("COACH", "Coach"),
        ("LEAGUE ADMIN", "LeagueAdmin"),
    ])

    # Override the init method
    def __init__(self, *args, **kwargs):
        # Call the init of the parent class
        super().__init__(*args, **kwargs)
        # Remove autofocus because it is in the wrong place
        del self.fields["username"].widget.attrs["autofocus"]

    # Put in custom signup logic
    def custom_signup(self, request, user):
        user.type = self.cleaned_data["type"]
        user.save()