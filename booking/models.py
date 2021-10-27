from django.db import models

# Create your models here.
class Doctor(models.Model):
    doctor_name = models.CharField(max_length=30)

class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField("date registered")
    waiting_status = models.BooleanField()

class Appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self
