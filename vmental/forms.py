from django.contrib.auth.forms import UserCreationForm
from vmental.models import PatientUser
from vmental.models import ProviderUser


class PatientCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = PatientUser
        fields = ('username', 'email', 'profile_img')

class ProviderCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ProviderUser
        fields = ('username', 'email', 'profile_img')