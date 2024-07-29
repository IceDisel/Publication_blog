from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from blog.forms import BlogPostForm
from blog.models import BlogPost
from users.models import User


class IndexView(TemplateView):
    """
    Контролер главной страницы.
    """

    template_name = "blog/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Многофункциональная платформа цифрового издательства для всех | Joomag'
        context['total_content'] = BlogPost.objects.all().count()
        context['premium_content'] = BlogPost.objects.filter(is_premium='True').count()
        context['all_users'] = User.objects.all().count()
        context['premium_user'] = User.objects.filter(is_premium='True').count()
        return context


class BlogCreateView(LoginRequiredMixin, CreateView):
    """
    Контролер создания публикации,
    для зарегистрированных пользователей.
    """

    model = BlogPost
    form_class = BlogPostForm
    success_url = reverse_lazy('blog:list')
    login_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class BlogListView(LoginRequiredMixin, ListView):
    """
    Контролер списка публикаций пользователя,
    для зарегистрированных пользователей.
    """

    model = BlogPost
    login_url = reverse_lazy('users:login')

    def get_queryset(self):
        if self.request.user.is_superuser:
            return BlogPost.objects.all()
        else:
            return BlogPost.objects.filter(author=self.request.user)


class BlogDetailView(DetailView):
    """
    Контролер просмотра публикации,
    для зарегистрированных пользователей.
    """

    model = BlogPost
    login_url = reverse_lazy('users:login')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Контролер редактирования публикации,
    для владельцев и администратора.
    """

    model = BlogPost
    form_class = BlogPostForm
    login_url = reverse_lazy('users:login')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

    def test_func(self):
        content = self.get_object()
        return self.request.user.is_superuser or self.request.user == content.author

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Контролер удаления публикации,
    для владельцев и администратора.
    """

    model = BlogPost
    success_url = reverse_lazy('blog:list')
    login_url = reverse_lazy('users:login')

    def test_func(self):
        content = self.get_object()
        return self.request.user.is_superuser or self.request.user == content.author


class BlogListAllView(ListView):
    """
    Контролер списка всех доступных публикаций.
    """

    model = BlogPost
    template_name = "blog/blogpost_all_list.html"

    def get_queryset(self):
        if self.request.user.is_authenticated and self.request.user.is_premium:
            return BlogPost.objects.all()
        else:
            return BlogPost.objects.exclude(is_premium=True)
