from django.shortcuts import render
from .models import Project

def project(request):
    projects = Project.objects.all().order_by('-created_at')[:4]
    return render(request, 'projectapp/projects.html', {'projects': projects})
