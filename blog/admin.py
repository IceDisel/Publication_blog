from django.contrib import admin

from blog.models import BlogPost


@admin.register(BlogPost)
class ContentAdmin(admin.ModelAdmin):
    """
    Отображение постов публикаций в админ панели.
    """

    list_display = ('id', 'title', 'content', 'created_date', 'views_count', 'author', 'is_premium')
