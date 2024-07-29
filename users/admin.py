from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Отображение пользователей в админ панели.
    """

    list_display = ('phone', 'password', 'nickname', 'phone', 'city', 'is_active', 'is_premium')
