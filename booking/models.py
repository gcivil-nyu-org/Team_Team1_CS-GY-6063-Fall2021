from account.models import CustomizedUser
from django.db import models
import datetime
from django.core.exceptions import ValidationError
from django.urls import reverse




class Appointment(models.Model):
    date = models.DateField()
    status_option = {
        ("active", "active"),
        ("cancelled", "cancelled"),
    }
    status = models.CharField(max_length=10, choices=status_option, default="active")
    def save(self, *args, **kwargs):
        if self.date < datetime.date.today():
            raise ValidationError("The date cannot in the past!")       
        return self.date
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
