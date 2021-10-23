from django.db import models
from vmental.models import CustomizedUser
from utils.time_helpers import utc_now


class Post(models.Model):
    author = models.ForeignKey(CustomizedUser,
        on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    @property
    def hours_to_now(self):
        # add utc time info
        return (utc_now() - self.created_at).seconds // 3600

    def __str__(self):
        return f'{self.created_at} {self.user}: {self.title} \n {self.content}'

