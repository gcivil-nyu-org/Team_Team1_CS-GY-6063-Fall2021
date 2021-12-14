from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from account.models import CustomizedUser


class DateInput(forms.DateInput):
    input_type = "date"


class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")
    phone_number = PhoneNumberField()

    class Meta(UserCreationForm.Meta):
        model = CustomizedUser
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "profile_img",
            "is_provider",
            "gender",
            "date_of_birth",
            "phone_number",
        )
        widgets = {
            "date_of_birth": DateInput(),
        }
