from django.contrib.auth.models import AbstractUser
from django.db.models.fields import BooleanField, CharField, DateField
from imagekit.models import ProcessedImageField


class CustomizedUser(AbstractUser):
    date_of_birth = DateField()
    GENDER_CHOICES = {
        ('M', 'Male'),
        ('F', 'Female'),
    }
    gender = CharField(max_length=1, choices=GENDER_CHOICES)
    is_provider = BooleanField()
    phone_number = CharField(max_length=10)
    profile_img = ProcessedImageField(
        upload_to='static/images/patient/profile_img',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )
