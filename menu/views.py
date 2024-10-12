from django.shortcuts import render, get_object_or_404
from .models import Dish

def home(request):
    # Пример: отображение популярных блюд
    dishes = Dish.objects.filter(available=True)
    return render(request, 'menu/home.html', {'dishes': dishes})

def dish_detail(request, id):
    dish = get_object_or_404(Dish, id=id)
    return render(request, 'menu/dish_detail.html', {'dish': dish})
