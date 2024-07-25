from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class BlogPost(models.Model):
    """
    Модель публикации.

    Атрибуты:
        title (CharField): Заголовок публикации.
        slug (CharField, опционально): Slug публикации.
        content (TextField): Содержимое публикации.
        preview (ImageField, опционально): Изображение превью публикации.
        created_date (DateTimeField): Дата создания публикации.
        is_premium (BooleanField): Является ли публикация премиум-публикацией.
        views_count (IntegerField): Количество просмотров публикации.
        author (ForeignKey): Автор публикации.
    """

    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='slug', **NULLABLE)
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(upload_to='previews/', verbose_name='Изображение', **NULLABLE)
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    is_premium = models.BooleanField(default=False, verbose_name='Премиум публикация')
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Автор')

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['title']

    def __str__(self):
        return self.title
