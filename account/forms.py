from django.contrib.auth.forms import UserCreationForm
from account.models import CustomizedUser
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta(UserCreationForm.Meta):
        model = CustomizedUser
        fields = (
            "email",
            "username",
            "profile_img",
            "first_name",
            "last_name",
            "gender",
            "is_provider",
            "date_of_birth",
            "phone_number",
        )
        widgets = {
            'date_of_birth': DateInput(),
        }
