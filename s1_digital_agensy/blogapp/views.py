from django.shortcuts import render

def blog(request):
    return render(request, 'blogapp/blog.html')
