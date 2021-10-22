from django.contrib import admin
from forum.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = (
        'created_at',
        'author',
        'title',
        'content',
    )