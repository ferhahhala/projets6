from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
from .models import Restaurant

def index_res(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index_res.html', {'restaurants': restaurants})