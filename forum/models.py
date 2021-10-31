from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from vmental.models import CustomizedUser
from utils.time_helpers import utc_now


class Post(models.Model):

    status_option = {
        ("draft", "draft"),
        ("published", "published"),
    }

    title = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255,
        unique=True,
        editable=False,
        default="",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        CustomizedUser,
        on_delete=models.CASCADE,
        null=True,
        related_name="posts",
    )
    content = models.TextField()
    status = models.CharField(max_length=10, choices=status_option, default="draft")

    def get_absolute_url(self):
        kwargs = {
            "pk": self.id,
            "slug": self.slug,
        }
        return reverse("post_detail_fbv", kwargs=kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)

    @property
    def hours_to_now(self):
        # add utc time info
        return (utc_now() - self.created_at).seconds // 3600

    def __str__(self):
        return f"{self.id} {self.author}: {self.title} \n {self.content}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    author = models.ForeignKey(
        CustomizedUser,
        on_delete=models.CASCADE,
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def hours_to_now(self):
        # add utc time info
        return (utc_now() - self.created_at).seconds // 3600

    def __str__(self):
        return f"{self.id} {self.author}: {self.post.id} \n {self.content}"
