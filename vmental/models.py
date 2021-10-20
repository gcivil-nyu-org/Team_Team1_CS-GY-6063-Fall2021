from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField


class BaseUser(AbstractUser):
    pass


class PatientUser(BaseUser):
    profile_img = ProcessedImageField(
        upload_to='static/images/patient/profile_img',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )


class ProviderUser(BaseUser):
    profile_img = ProcessedImageField(
        upload_to='static/images/provider/profile_img',
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )
