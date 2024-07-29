from django.test import TestCase, Client
from django.urls import reverse

from blog.models import BlogPost
from users.models import User


class PublicationViewTest(TestCase):
    """
    Тестирование приложения blog.
    """

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(phone='+79123456789', password='qwerty123', is_active=True)
        self.content = BlogPost.objects.create(title='Заголовок публикации', content='Контент публикации',
                                               author=self.user, is_premium=True)
        self.client.force_login(user=self.user)

    def test_create_blog(self):
        """
        Тестирование контролера создания публикации.
        """

        url = reverse('blog:create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/blogpost_form.html')
        data = {
            'title': 'Новый заголовок публикации',
            'content': 'Новый контент публикации',
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('blog:list'))
        self.assertEqual(BlogPost.objects.all().filter(author_id=self.user).first().content,
                         'Контент публикации')
        self.assertEqual(BlogPost.objects.all().filter(author_id=self.user).count(), 2)

    def test_blog_list(self):
        """
        Тестирование контролера списка публикаций.
        """

        url = reverse('blog:list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(BlogPost.objects.count(), 1)

    def test_update_blog(self):
        """
        Тестирование контролера обновления публикации.
        """

        url = reverse('blog:edit', args=[self.content.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = {
            'title': 'Заголовок публикации',
            'content': '9 способов научиться программировать',
        }
        response = self.client.post(url, data)
        self.content.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.content.content, '9 способов научиться программировать')

    def test_delete_blog(self):
        """
        Тестирование контролера удаления публикации.
        """

        url = reverse('blog:delete', args=[self.content.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.client.delete(url)
        self.assertEqual(BlogPost.objects.count(), 0)

    def test_blog_list_all(self):
        """
        Тестирование контролера списка публикаций всех авторов.
        """

        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
