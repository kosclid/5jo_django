from django.contrib.auth.forms import *
from accounts.models import User


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "gender",
            "age",
        )
        pass

    field_order = ["username", "password1", "password2", "gender", "age"]
    pass
