from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserUpdateView, phone_verification, generate_new_password, payment_create, \
    payment_success, payment_cancel

app_name = UsersConfig.name

urlpatterns = [
    path('login', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('phone-verify/', phone_verification, name='phone_verify'),
    path('profile/', UserUpdateView.as_view(), name='profile'),
    path('profile/new-password', generate_new_password, name='new_password'),

    path('payment_create/', payment_create, name='payment_create'),
    path('payment_success/', payment_success, name='payment_success'),
    path('payment_cancel/', payment_cancel, name='payment_cancel'),
]
