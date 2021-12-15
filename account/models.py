import datetime

from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, RegexValidator
from django.db.models.fields import BooleanField, CharField, DateField, EmailField
from imagekit.models import ProcessedImageField


class CustomizedUser(AbstractUser):
    email = EmailField(max_length=200, unique=True)
    date_of_birth = DateField(
        validators=[MaxValueValidator(limit_value=datetime.date.today())],
        null=True,
        blank=True,
    )
    GENDER_CHOICES = {
        ("M", "Male"),
        ("F", "Female"),
    }
    gender = CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    is_provider = BooleanField(default=False)
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone_number = CharField(
        validators=[phone_number_regex], max_length=16, null=True, blank=True
    )
    profile_img = ProcessedImageField(
        upload_to="static/images/patient/profile_img",
        format="JPEG",
        options={"quality": 100},
        blank=True,
        null=True,
    )
