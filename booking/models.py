<<<<<<< HEAD
from django.db import models
from django.urls import reverse


# from django.contrib.auth import user_logged_in
=======
>>>>>>> 10e95c76ff4ba429e41bcf1edcb46209ab5c65c6
from account.models import CustomizedUser
from django.db import models


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
    meeting_link = models.URLField(blank=True)
    status_option = {
        ("active", "active"),
        ("cancelled", "cancelled"),
    }
    status = models.CharField(max_length=10, choices=status_option, default="active")
