from django.db import models

# from django.contrib.auth import user_logged_in
from account.models import CustomizedUser


class Appointment(models.Model):
    status_option = {
        ("available", "available"),
        ("confirmed", "confirmed"),
    }
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(
        CustomizedUser, on_delete=models.CASCADE, null=True, related_name="user"
    )
    doctor = models.ForeignKey(
        CustomizedUser, on_delete=models.CASCADE, related_name="doctor"
    )
    status = models.CharField(max_length=10, choices=status_option, default="available")

    def __main__(self):
        return self


class provider_timeSlots(models.Model):
    date = (models.DateField(),)
    time_from = (models.TimeField(),)
    time_to = models.TimeField()
