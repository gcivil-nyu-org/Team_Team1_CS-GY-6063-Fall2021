from django.contrib.auth.forms import UserCreationForm
from vmental.models import CustomizedUser


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomizedUser
        fields = (
            'email',
            'username',
            'password',
            'profile_img',
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'phone_number',
        )
