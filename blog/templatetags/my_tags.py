from django import template

register = template.Library()


@register.filter()
# @register.simple_tag()
def my_media(data):
    """
    Тег для направления пути к медиа файлам
    """
    if data:
        return f'/media/{data}'
    return '/static/img/white.jpg'
