from django.contrib import admin

from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = "id", "title", "created_on"
    list_display_links = "id", "title"


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = "id", "author", "post", "content"
    list_display_links = "id", "content"
