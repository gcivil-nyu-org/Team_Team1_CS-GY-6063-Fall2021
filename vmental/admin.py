from django.contrib import admin
from vmental.models import CustomizedUser


@admin.register(CustomizedUser)
class CustomizedUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
    )
