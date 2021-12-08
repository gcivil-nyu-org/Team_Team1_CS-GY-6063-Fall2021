import datetime

from django.core.exceptions import ValidationError

from account.models import CustomizedUser
from django.core.validators import MinValueValidator
from django.db import models

from utils.time_helpers import utc_now


class Appointment(models.Model):
    date = models.DateField(validators=[MinValueValidator(limit_value=utc_now().date() + datetime.timedelta(days=1))])
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(
        CustomizedUser, on_delete=models.CASCADE, related_name="doctor"
    )
    patient = models.ForeignKey(
        CustomizedUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="patient",
    )
    meeting_link = models.URLField(blank=True)
    status_option = {
        ("active", "active"),
        ("cancelled", "cancelled"),
    }
    status = models.CharField(max_length=10, choices=status_option, default="active")
