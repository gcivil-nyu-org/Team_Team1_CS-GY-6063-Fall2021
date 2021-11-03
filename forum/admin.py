from django.contrib import admin
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
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "post",
        "author",
        "created_at",
        "content",
    )
