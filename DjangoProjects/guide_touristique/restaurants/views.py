from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    wilaya = request.GET.get('wilaya')

    restaurants = Restaurant.objects.all()
    if wilaya:
        restaurants = restaurants.filter(wilaya__icontains=wilaya)

    # ترتيب تلقائي حسب السعر تصاعديًا
    restaurants = restaurants.order_by('price')

    return render(request, 'core/list_template.html', {
        'items': restaurants,
        'wilaya': wilaya,
        'category_name': 'Restaurants',
        'max_price': None
    })