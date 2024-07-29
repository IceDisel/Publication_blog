from django.test import TestCase, Client
from django.urls import reverse

from users.models import User


class UserTest(TestCase):
    """
    Тестирование приложения users.
    """

    def setUp(self):
        self.client = Client()

    def test_user_register(self):
        """
        Тест регистрации пользователя.
        """

        url = reverse('users:registration')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user_register_form.html')
        data = {
            'phone': '+78003456789',
            'nickname': 'Petya34',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(url, data)
        self.assertTrue(User.objects.filter(nickname='Petya34').exists())
        self.assertEqual(response.status_code, 302)

    def test_user_update(self):
        """
        Тест обновления пользователя.
        """

        data = {
            'phone': '++78003456789',
            'nickname': 'Petya34',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        self.client.post(reverse('users:registration'), data)

        new_user = User.objects.all().filter(nickname='Petya34').first()
        url = reverse('users:profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
        data = {
            'phone': '++78003456789',
            'nickname': 'Vasya34',
        }
        response = self.client.post(url, data)
        new_user.refresh_from_db()
        self.assertEqual(response.status_code, 302)
