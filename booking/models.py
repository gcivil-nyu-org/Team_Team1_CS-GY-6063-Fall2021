from account.models import CustomizedUser
from django.db import models
import datetime
from django.core.exceptions import ValidationError



class Appointment(models.Model):
    date = models.DateField()
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
    meeting_link = models.URLField(blank=True,null=True)
    status_option = {
        ("active", "active"),
        ("cancelled", "cancelled"),
    }
    status = models.CharField(max_length=10, choices=status_option, default="active")
    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot in the past!")       
        return self.date