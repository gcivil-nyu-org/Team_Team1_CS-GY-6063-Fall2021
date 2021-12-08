import datetime

from django.core.exceptions import ValidationError

from account.models import CustomizedUser
from django.core.validators import MinValueValidator
from django.db import models


class Appointment(models.Model):
    date = models.DateField(validators=[MinValueValidator(limit_value=(datetime.date.today()))])
    start_time = models.TimeField(validators=[MinValueValidator(limit_value=datetime.datetime.now().time())])
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
        ("expired", "expired"),
        ("cancelled", "cancelled"),
    }
    status = models.CharField(max_length=10, choices=status_option, default="active")

    def clean(self):
        if self.date <= datetime.date.today() or self.start_time <= datetime.datetime.now().time() or self.end_time <= self.start_time:
            raise ValidationError("Invalid appointment time")