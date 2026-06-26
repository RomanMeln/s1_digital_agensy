from django.shortcuts import render
from .models import Post, CategoryName


def blog(request):
    posts = Post.objects.all().order_by('-created_at')[:4]
    categories = CategoryName.objects.all()
    # проверка наличия статьи
    if posts:
        default_post = posts[0] # дефолтный пост
    else:
        # если постов нет
        default_post = Post(
            title="Заголовок новой статьи",
            text="Текст появится, когда вы добавите статьи в админ-панель."
            # description и image подставятся автоматически из дефолтов модели!
        )

        # Добавляем его в список, чтобы posts.0 на главной странице не вызвал ошибку
        posts.append(default_post)

    return render(request, 'blogapp/blog.html', {'posts': posts,
                                                 'def_post': default_post, 'categories': categories})
