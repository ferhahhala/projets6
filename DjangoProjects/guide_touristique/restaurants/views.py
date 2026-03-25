from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    wilaya = request.GET.get('wilaya')
    r_type = request.GET.get('type')
    query = request.GET.get('q', '')   # 🔥 هذا هو المهم

    restaurants = Restaurant.objects.all()

    if wilaya:
        restaurants = restaurants.filter(wilaya__icontains=wilaya)

    if r_type:
        restaurants = restaurants.filter(type=r_type)

    # 🔥 search بالاسم
    if query:
        restaurants = restaurants.filter(name__icontains=query)

    restaurants = restaurants.order_by('price')

    return render(request, 'core/list_template.html', {
        'items': restaurants,
        'wilaya': wilaya,
        'query': query,   # 🔥 مهم باش يرجع في input
        'category_name': r_type.capitalize() if r_type else 'Restaurants',
        'max_price': None,
        'show_footer': True
    })