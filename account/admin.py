from django.contrib import admin
from account.models import CustomizedUser

admin.site.register(CustomizedUser, )
@admin.register(CustomizedUser)
class CustomizedUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
    )
