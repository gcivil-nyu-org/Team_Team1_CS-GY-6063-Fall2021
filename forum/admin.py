from django.contrib import admin
from forum.models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_display = (
        "id",
        "created_at",
        "author",
        "title",
        "content",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "post",
        "author",
        "content",
    )
