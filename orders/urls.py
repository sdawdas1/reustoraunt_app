from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_order, name='create_order'),  # Создание заказа
    path('history/', views.order_history, name='order_history'),  # История заказов
]
