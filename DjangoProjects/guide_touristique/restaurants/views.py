from django.shortcuts import render
from .models import Restaurant

def restaurant_list(request):
    wilaya = request.GET.get('wilaya')
    query = request.GET.get('q', '')
    r_type = request.GET.get('type')  # ✅ لازم تضيف هذا

    restaurants = Restaurant.objects.all()

    if wilaya:
        restaurants = restaurants.filter(wilaya__icontains=wilaya)

    if r_type:
        restaurants = restaurants.filter(type=r_type)

    if query:
        restaurants = restaurants.filter(name__icontains=query)
        print("TYPE:", r_type)
        print("WILAYA:", wilaya)

    return render(request, 'core/list_template.html', {
        'items': restaurants,
        'wilaya': wilaya,
        'query': query,
        'category_name': r_type.capitalize() if r_type else 'Restaurants',
        'show_footer': True
    })