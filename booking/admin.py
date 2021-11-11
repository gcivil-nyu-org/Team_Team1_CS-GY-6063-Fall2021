from django.contrib import admin

from booking.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ("id", "date", "time", "doctor", "user", "status")
