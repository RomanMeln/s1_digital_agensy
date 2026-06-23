from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(max_length=200, verbose_name='Краткое описание', default='Краткое описание')
    text = models.TextField(verbose_name='Текст о проекте')
    image = models.ImageField(verbose_name='Фотография', upload_to='project_photos/', default='progect_photos/default.png')
    created_at = models.DateTimeField(verbose_name='Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']
