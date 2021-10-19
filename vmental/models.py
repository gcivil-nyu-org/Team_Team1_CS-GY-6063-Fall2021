from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from imagekit.models import ProcessedImageField
    
class PatientUser(AbstractUser):
    profile_img = ProcessedImageField(
        upload_to='static/images/patient/profile_img',
        format='JPEG',
        options={'quality':100},
        blank=True,
        null=True
    )