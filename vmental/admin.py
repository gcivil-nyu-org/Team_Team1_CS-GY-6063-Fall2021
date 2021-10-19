from django.contrib import admin
from vmental.models import PatientUser
from vmental.models import ProviderUser

# Register your models here.
admin.site.register(PatientUser)
admin.site.register(ProviderUser) 
