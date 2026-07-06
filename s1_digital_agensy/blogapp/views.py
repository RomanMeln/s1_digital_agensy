from django.shortcuts import render, get_object_or_404
from .models import Post, CategoryName


# def blog(request):
#     posts = Post.objects.all().order_by('-created_at')[:4]
#     categories = CategoryName.objects.all()
#     # проверка наличия статьи
#     if posts:
#         default_post = posts[0] # дефолтный пост
#     else:
#         # если постов нет
#         default_post = Post(
#             title="Заголовок новой статьи",
#             text="Текст появится, когда вы добавите статьи в админ-панель."
#             # description и image подставятся автоматически из дефолтов модели!
#         )
#
#         # Добавляем его в список, чтобы posts.0 на главной странице не вызвал ошибку
#         posts.append(default_post)
#
#     return render(request, 'blogapp/blog.html', {'posts': posts,
#                                                  'def_post': default_post, 'categories': categories})

def blog(request):
    # Получаем ID категории из GET-запроса (?category=ID)
    category_id = request.GET.get('category')

    # Оптимизируем запрос через select_related (загружаем пост вместе с его категорией за 1 запрос)
    posts_queryset = Post.objects.all().select_related('category').order_by('-created_at')

    # Фильтруем, если ID передан и это число
    if category_id and category_id.isdigit():
        posts_queryset = posts_queryset.filter(category_id=int(category_id))

    # Забираем максимум 4 поста и превращаем QuerySet в обычный список Python
    posts = list(posts_queryset[:4])
    categories = CategoryName.objects.all()

    # Создаем дефолтный пост на случай, если постов не хватает
    default_post = Post(
        title="Заголовок новой статьи",
        description="Текст появится, когда вы добавите статьи в админ-панель.",
        text="Полный текст статьи."
    )
    # Создаем временный объект категории для дефолтного поста, чтобы template не падал
    default_post.category = CategoryName(name="Маркетинг")

    # Безопасность шаблона: добиваем список до 4 элементов дефолтными постами
    while len(posts) < 4:
        posts.append(default_post)

    # Передаем ID текущей категории в контекст как число (или None), чтобы подсветить фильтр в HTML
    if category_id and category_id.isdigit():
        current_category = int(category_id)
    else:
        current_category = None

    context = {
        'posts': posts,
        'def_post': posts[0],  # Самый первый пост
        'categories': categories,
        'current_category': current_category,
    }

    return render(request, 'blogapp/blog.html', context)


def post_detail(request, post_id):
    # Находим статью по ID или отдаем ошибку 404, если её нет
    post = get_object_or_404(Post.objects.select_related('category'), id=post_id)

    context = {
        'post': post
    }
    return render(request, 'blogapp/post_detail.html', context)
