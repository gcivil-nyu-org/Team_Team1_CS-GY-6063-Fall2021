from django.db import models
from django.urls import reverse


# from django.contrib.auth import user_logged_in
from account.models import CustomizedUser


class Appointment(models.Model):
    status_option = {
        ("available", "available"),
        ("confirmed", "confirmed"),
    }
    date = models.DateField()
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    patient = models.ForeignKey(
        CustomizedUser, on_delete=models.SET_NULL,null=True, blank=True, related_name="patient"
    )
    doctor = models.ForeignKey(
        CustomizedUser, on_delete=models.CASCADE, related_name="doctor"
    )
    
    meeting_link = models.URLField(null=True)

    def __main__(self):
        return self
    
    def get_absolute_url(self):
        return reverse('my_availability')


class provider_timeSlots(models.Model):
    date = (models.DateField(),)
    time_from = (models.TimeField(),)
    time_to = models.TimeField()
