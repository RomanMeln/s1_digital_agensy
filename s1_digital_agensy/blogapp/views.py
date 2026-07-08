from django.shortcuts import render, get_object_or_404
from .models import Post, CategoryName


def blog(request):
    # Получает ID категории из GET-запроса (?category=ID)
    category_id = request.GET.get('category')

    # Оптимизирует запрос через select_related (загружает пост вместе с его категорией за 1 запрос)
    posts_queryset = Post.objects.all().select_related('category').order_by('-created_at')

    # Фильтрует, если ID передан и это число
    if category_id and category_id.isdigit():
        posts_queryset = posts_queryset.filter(category_id=int(category_id))

    # Забирает максимум 4 поста и превращает QuerySet в обычный список Python
    posts = list(posts_queryset[:4])
    categories = CategoryName.objects.all()

    # Создает дефолтный пост на случай, если постов не хватает
    default_post = Post(
        title="Заголовок новой статьи",
        description="Текст появится, когда вы добавите статьи в админ-панель.",
        text="Полный текст статьи."
    )
    # Создает временный объект категории для дефолтного поста, чтобы template не падал
    default_post.category = CategoryName(name="Маркетинг")

    if posts:  # проверяет, что в категории есть хотя бы один пост
        real_posts_count = len(posts)
        while len(posts) < 4:
            # берет посты по кругу (0, 1, 2...) из тех, что нашлись
            posts.append(posts[len(posts) % real_posts_count])
    else:
        # если вообще нет постов, тогда уже используем заглушку
        while len(posts) < 4:
            posts.append(default_post)

    # Передает ID текущей категории в контекст как число (или None), чтобы подсветить фильтр в HTML
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
    # Находит статью по ID или отдаем ошибку 404, если её нет
    post = get_object_or_404(Post.objects.select_related('category'), id=post_id)

    context = {
        'post': post
    }
    return render(request, 'blogapp/post_detail.html', context)
