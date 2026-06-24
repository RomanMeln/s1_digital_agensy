from django.shortcuts import render
from .models import Post, CategoryName


def blog(request):
    posts = Post.objects.all().order_by('-created_at')[:4]
    return render(request, 'blogapp/blog.html', {'posts': posts})
