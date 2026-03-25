from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    wilaya = request.GET.get('wilaya')
    r_type = request.GET.get('type')  # type=restaurant أو type=fastfood

    restaurants = Restaurant.objects.all()
    if wilaya:
        restaurants = restaurants.filter(wilaya__icontains=wilaya)
    if r_type:
        restaurants = restaurants.filter(type=r_type)

    restaurants = restaurants.order_by('price')

    return render(request, 'core/list_template.html', {
        'items': restaurants,
        'wilaya': wilaya,
        'category_name': r_type.capitalize() if r_type else 'Restaurants',
        'max_price': None
    })