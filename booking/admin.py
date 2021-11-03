from django.contrib import admin

from booking.models import Appointments

# Register your models here.


@admin.register(Appointments)
class Appointments(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "time",
        "doctor",
        "user",
        "status"
    )
