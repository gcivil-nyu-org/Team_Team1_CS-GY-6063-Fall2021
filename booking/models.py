from django.db import models
from forum.models import Post
#from django.contrib.auth import user_logged_in
from vmental.models import CustomizedUser

class Doctor(models.Model):  # E302
    doctor_name = models.CharField(max_length=30)
    


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField("date registered")
    waiting_status = models.BooleanField()


class Appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(CustomizedUser, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __main__(self):
        return self
