from django.shortcuts import render # pyright: ignore[reportMissingModuleSource]
from .models import Restaurant

def restaurents_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index_res.html', {'restaurants': restaurants})