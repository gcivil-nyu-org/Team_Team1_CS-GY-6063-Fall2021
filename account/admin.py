from django.contrib import admin
from account.models import CustomizedUser
from django.contrib.auth.admin import UserAdmin


# @admin.register(CustomizedUser)
# class CustomizedUserAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "username",
#     )
admin.site.register(CustomizedUser, UserAdmin)