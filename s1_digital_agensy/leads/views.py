from django.shortcuts import redirect
from django.contrib import messages
from .forms import ProjectStartForm


def submit_proposal(request):
    if request.method == 'POST':
        # создает форму и наполняет её данными из POST-запроса
        form = ProjectStartForm(request.POST)

        # is_valid() автоматически запустит clean_name() и clean_contact() из формы выше
        if form.is_valid():
            form.save()
            messages.success(request, "Заявка успешно отправлена!")
        else:
            # Если возникли ошибки, Django добавит их в форму
            messages.error(request, "Ошибка заполнения формы. Проверьте введенные данные.")

    # Возвращает пользователя обратно на ту страницу, откуда он пришел
    return redirect(request.META.get('HTTP_REFERER', '/'))
