from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),  # Регистрация
    path('login/', views.login_view, name='login'),  # Вход
    path('logout/', views.logout_view, name='logout'),  # Выход
    path('profile/', views.profile, name='profile'),  # Профиль пользователя
]
