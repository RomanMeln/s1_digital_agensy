from django.contrib import admin
from .models import Post
from .models import CategoryName


@admin.register(CategoryName)
class CategoryNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('category__name','created_at')
    search_fields = ('category', 'title')
    ordering = ('-created_at',)
    list_select_related = ('category',)
