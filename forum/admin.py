from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from forum.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "id",
        "title",
        "slug",
        "created_at",
        "author",
        "content",
        "status",
    )


@admin.register(Comment)
class CommentAdmin(MPTTModelAdmin):
    list_display = (
        "id",
        "post",
        "author",
        "created_at",
        "content",
    )
