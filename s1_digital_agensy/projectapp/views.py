from django.shortcuts import render, get_object_or_404
from .models import Project

def project(request):
    projects = Project.objects.all().order_by('-created_at')[:4]

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
    return render(request, 'projectapp/projects.html', {'projects': projects,
                                                        'def_project': default_project})

def case(request, pk):
    selected_case = get_object_or_404(Project, pk=pk)
    
    context = {
        'selected_case': selected_case
    }
    return render(request, 'projectapp/case.html', context)
