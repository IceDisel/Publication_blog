from django import forms

from blog.models import BlogPost


class StyleFormMixin:
    """
    Миксин для добавления стилей к форме.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class BlogPostForm(StyleFormMixin, forms.ModelForm):
    """
    Класс для отображения формы модели публикации
    """

    class Meta:
        model = BlogPost
        exclude = ['created_date', 'views_count', 'author', 'slug']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

        if not self.user.is_premium:
            del self.fields['is_premium']
