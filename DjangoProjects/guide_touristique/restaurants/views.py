from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
from .models import Restaurant

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurants_list.html', {'restaurants': restaurants})