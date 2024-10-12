from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:dish_id>/', views.add_review, name='add_review'),  # Добавление отзыва
    path('edit/<int:review_id>/', views.edit_review, name='edit_review'),  # Редактирование отзыва
]
