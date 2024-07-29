from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Команда создания супер пользователя (python manage.py csu).
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            phone="+79002000600",
            nickname='superuser',
            is_active=True,
            is_staff=True,
            is_premium=True,
            is_superuser=True
        )

        user.set_password("123456")

        user.save()
