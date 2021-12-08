from django.contrib.auth.models import AbstractUser
from django.db.models.fields import (
    BooleanField,
    CharField,
    DateField,
    EmailField,
)
from imagekit.models import ProcessedImageField
from django.core.validators import MaxValueValidator
from datetime import date
from phonenumber_field.modelfields import PhoneNumberField


class CustomizedUser(AbstractUser):
    email = EmailField(max_length=200, unique=True)
    date_of_birth = DateField(validators=[MaxValueValidator(limit_value=date.today)])
    GENDER_CHOICES = {
        ("M", "Male"),
        ("F", "Female"),
    }
    gender = CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    is_provider = BooleanField(default=False)
    phone_number = PhoneNumberField(max_length=10, blank=True)
    profile_img = ProcessedImageField(
        upload_to="static/images/patient/profile_img",
        format="JPEG",
        options={"quality": 100},
        blank=True,
        null=True,
    )
