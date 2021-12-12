import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db.models.fields import BooleanField, CharField, DateField, EmailField
from imagekit.models import ProcessedImageField


class CustomizedUser(AbstractUser):
    email = EmailField(max_length=200, unique=True)
    date_of_birth = DateField(
        validators=[MaxValueValidator(limit_value=datetime.date.today())], null=True
    )
    GENDER_CHOICES = {
        ("M", "Male"),
        ("F", "Female"),
    }
    gender = CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    is_provider = BooleanField(default=False)
    phone_number = CharField(max_length=10, blank=True)
    profile_img = ProcessedImageField(
        upload_to="static/images/patient/profile_img",
        format="JPEG",
        options={"quality": 100},
        blank=True,
        null=True,
    )
