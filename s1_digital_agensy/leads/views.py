from django.shortcuts import render, redirect
from .forms import ProjectStartForm


def submit_proposal(request):
    if request.method == 'POST':
        form = ProjectStartForm(request.POST)

        if form.is_valid():
            form.save()
            # УСПЕХ
            return render(request, 'mainapp/application-success.html')

        else:
            # ОШИБКА
            return render(request, 'mainapp/application-error.html', {'form': form})

    return redirect('/')
