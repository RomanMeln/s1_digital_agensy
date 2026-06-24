from django.db import models


class CategoryName(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    category = models.ForeignKey(CategoryName, on_delete=models.PROTECT, verbose_name="Категория")
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(max_length=200, verbose_name='Описание', default='Тут должно быть описание')
    text = models.TextField(verbose_name='Текст статьи')
    image = models.ImageField(verbose_name='Фотография', upload_to='blog_photos/', default='blog_photos/default.png')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)
    is_main = models.BooleanField(default=False)  # Чтобы отметить главную новость

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья/Пост'
        verbose_name_plural = 'Статьи/Посты'
        ordering = ['-created_at']
