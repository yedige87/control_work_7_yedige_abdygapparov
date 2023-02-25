from django.db import models


# Create your models here.
class GBook(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, verbose_name='Имя пользователя')
    email = models.CharField(max_length=30, null=False, blank=False, verbose_name='EMail пользователя')
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Сообщение пользователя')
    status = models.CharField(max_length=20, null=False, blank=False, verbose_name='Статус пользователя', default='active')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f"{self.name} - {self.email}"

    class Meta:
        verbose_name = 'Пользователи'
        verbose_name_plural = 'Пользователи'
        ordering = ['-created_at']