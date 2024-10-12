from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('dish/<int:id>/', views.dish_detail, name='dish_detail'),  # Детали блюда
]
