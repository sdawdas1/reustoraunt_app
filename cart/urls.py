from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_cart, name='view_cart'),  # Просмотр корзины
    path('add/<int:dish_id>/', views.add_to_cart, name='add_to_cart'),  # Добавление в корзину
    path('remove/<int:dish_id>/', views.remove_from_cart, name='remove_from_cart'),  # Удаление из корзины
]
