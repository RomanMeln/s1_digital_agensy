from django.db import models


class ProjectStart(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.CharField(verbose_name="Контактные данные (Email или телефон)",null=True, blank=True)
    message = models.TextField(verbose_name="Текст заявки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"Заявка от {self.name} ({self.contact})"

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']
