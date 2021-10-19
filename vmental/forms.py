from django.contrib.auth.forms import UserCreationForm
from vmental.models import PatientUser


class PatientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PatientUser
        fields = ('username', 'email', 'profile_img')
