from django.contrib.auth.forms import UserCreationForm
from vmental.models import CustomizedUser


class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomizedUser
        fields = (
            'email',
            'username',
            'profile_img',
            'first_name',
            'last_name',
            'gender',
            'is_provider',
            'date_of_birth',
            'phone_number',
        )
