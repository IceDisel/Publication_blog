from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from blog.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Класс для отображения формы модели регистрации
    """

    class Meta:
        model = User
        fields = ('phone', 'nickname', 'password1', 'password2')


class UserForm(StyleFormMixin, UserChangeForm):
    """
    Класс для отображения формы модели пользователя
    """

    class Meta:
        model = User
        fields = ('nickname', 'phone', 'city', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()