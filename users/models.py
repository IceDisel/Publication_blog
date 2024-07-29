from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """
    Модель пользователя.

    Атрибуты:
        phone (PhoneNumberField): Номер телефона пользователя.
        nickname (CharField): Псевдоним пользователя.
        city (CharField, опционально): Город пользователя.
        is_premium (BooleanField): Является ли пользователь премиум-пользователем.
        is_active (BooleanField): Является ли пользователь активным.
        token (CharField, опционально): Токен пользователя.
        payment_session_id (CharField, опционально): ID сессии оплаты пользователя.
    """
    username = None

    phone = PhoneNumberField(region='RU', verbose_name='Номер телефона', unique=True)
    nickname = models.CharField(max_length=200, verbose_name='Псевдоним', unique=True)
    city = models.CharField(max_length=50, verbose_name='Город', **NULLABLE)
    is_premium = models.BooleanField(default=False, verbose_name='Премиум пользователь')
    is_active = models.BooleanField(default=False, verbose_name='Активный пользователь')
    token = models.CharField(max_length=100, verbose_name='Токен', **NULLABLE)
    payment_session_id = models.CharField(max_length=300, verbose_name='ID сессии оплаты', **NULLABLE)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.nickname}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
