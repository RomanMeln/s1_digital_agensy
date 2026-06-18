from django.contrib import admin
from .models import Post


admin.site.register(Post)

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'service_type', 'created_at']
#     list_display_links = ['id', 'title']
#     list_filter = ['service_type','created_at']
#     search_fields = ['title', 'description']
#     ordering = ['-created_at']