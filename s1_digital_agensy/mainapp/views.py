from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def products(request):
    return render(request, 'mainapp/projects.html')


def contacts(request):
    return render(request, 'mainapp/contacts.html')

def about_us(request):
    return render(request, 'mainapp/about_us.html')

def blog(request):
    return render(request, 'mainapp/blog.html')

def services(request):
    return render(request, 'mainapp/services.html')

def cases(request):
    return render(request, 'mainapp/cases.html')
