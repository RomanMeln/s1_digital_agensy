from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('category','created_at')
    search_fields = ('category', 'title')
    ordering = ('-created_at',)
