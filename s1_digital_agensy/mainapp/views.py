from django.shortcuts import render
from .models import ProjectStart
from blogapp.models import Post, CategoryName
from projectapp.models import Project


def index(request):
    projects = Project.objects.all().order_by('-created_at')[:5]

    if projects:
        default_project = projects[0] # дефолтный проект
    else:
        # если проектов нет
        default_project = Project(
            title="Тут должно быть название проекта",
            text="Тут должно все о проекте"
            # description и image подставятся автоматически из дефолтов модели!
        )

        # Добавляем его в список, чтобы posts.0 на главной странице не вызвал ошибку
        projects.append(default_project)

    posts = Post.objects.all().order_by('-created_at')[:5]
    # проверка наличия статьи
    if posts:
        default_post = posts[0]  # дефолтный пост
    else:
        # если постов нет
        default_post = Post(
            title="Заголовок новой статьи",
            text="Текст появится, когда вы добавите статьи в админ-панель."
            # description и image подставятся автоматически из дефолтов модели!
        )

        # Добавляем его в список, чтобы posts.0 на главной странице не вызвал ошибку
        posts.append(default_post)

    return render(request, 'mainapp/index.html', {'posts': posts, 'def_post': default_post,
                                                  'projects': projects, 'def_project': default_project})

def contacts(request):
    return render(request, 'mainapp/contacts.html')

def about_us(request):
    return render(request, 'mainapp/about_us.html')

def services(request):
    return render(request, 'mainapp/services.html')

def cases(request):
    return render(request, 'mainapp/cases.html')

def contact_us_email(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Вывести в консоль для теста:
        project_sql = ProjectStart.objects.create(
            name=name,
            contact=email,
            message=message
        )
        print(f"Новое сообщение от {name} ({email}): {message}")
        print(f"Сохранено в БД с ID: {project_sql.pk}")

        return render(request, 'mainapp/application-success.html')

    return render(request, 'mainapp/contact-us.html')


def contact_us_phone(request):
    if request.method == "POST":
        # Забираем данные из HTML-полей
        name = request.POST.get('name')
        phone = request.POST.get('email')
        message = request.POST.get('message')


        project_sql = ProjectStart.objects.create(
            name=name,
            contact=phone,
            message=message
        )

        print(f"Новое сообщение от {name} ({phone}): {message}")
        print(f"Сохранено в БД с ID: {project_sql.pk}")

        return render(request, 'mainapp/application-success.html')

    return render(request, 'mainapp/contact-us.html')
