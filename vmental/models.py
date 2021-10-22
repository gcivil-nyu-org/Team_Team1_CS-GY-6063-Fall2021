from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, CharField, DateField
from imagekit.models import ProcessedImageField


class CustomizedUser(AbstractUser):
    date_of_birth = DateField(blank=True, null=True)
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
    }
    gender = CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    is_provider = BooleanField(default=False)
    phone_number = CharField(max_length=10, blank=True)
    profile_img = ProcessedImageField(
        upload_to='static/images/patient/profile_img',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )
