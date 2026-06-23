from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('title','created_at')
    search_fields = ('title',)
    ordering = ('-created_at',)

