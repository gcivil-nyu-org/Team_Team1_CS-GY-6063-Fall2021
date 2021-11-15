from django.contrib import admin

from booking.models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "start_time",
        "end_time",
        "doctor",
        "patient",
        "meeting_link",
    )
