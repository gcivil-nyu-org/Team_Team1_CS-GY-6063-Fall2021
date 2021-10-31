from django.contrib import admin
from forum.models import Post, Comment


@admin.register(Post)
class PostFBVAdmin(admin.ModelAdmin):
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
        "created_at",
        "post",
        "author",
        "content",
    )
