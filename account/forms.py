from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import CustomizedUser


class DateInput(forms.DateInput):
    input_type = "date"


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta(UserCreationForm.Meta):
        model = CustomizedUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "gender",
            "date_of_birth",
            "profile_img",
            "is_provider",
            "phone_number",
        )
        widgets = {
            "date_of_birth": DateInput(),
        }
