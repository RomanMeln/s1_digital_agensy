from django.shortcuts import render
from .models import ProjectStart


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

def contact_us(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Вывести в консоль для теста:
        project_sql = ProjectStart.objects.create(
            name=name,
            email=email,
            message=message
        )
        print(f"Новое сообщение от {name} ({email}): {message}")
        print(f"Сохранено в БД с ID: {project_sql.pk}")

        return render(request, 'mainapp/application-success.html')

    return render(request, 'mainapp/contact-us.html')
