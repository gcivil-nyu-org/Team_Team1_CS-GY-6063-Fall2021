from django.contrib import admin

from booking.models import Doctor,Appointments,Patient
# Register your models here.

@admin.register(Appointments)
class Appointments(admin.ModelAdmin):
    list_display = (
        "date",
        "time",
        "doctor",
    )

@admin.register(Doctor)
class Doctor(admin.ModelAdmin):
    list_display = (
        "doctor_name",
    )