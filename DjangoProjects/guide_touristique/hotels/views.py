from django.shortcuts import render
from .models import Hotel

def hotel_list(request):
    wilaya = request.GET.get('wilaya')
    query = request.GET.get('q', '')
    max_price = request.GET.get('max_price')  # 🔥 أضف هذا

    hotels = Hotel.objects.all()

    # 📍 filtre wilaya
    if wilaya:
        hotels = hotels.filter(wilaya__icontains=wilaya)

    # 🔍 search
    if query:
        hotels = hotels.filter(name__icontains=query)

    # 💰 filtre prix
    if max_price:
        hotels = hotels.filter(price__lte=max_price)

    # 🔥 ترتيب
    hotels = hotels.order_by('price')

    return render(request, 'core/list_template.html', {
        'items': hotels,
        'wilaya': wilaya,
        'query': query,
        'max_price': max_price,  # 🔥 مهم
        'category_name': 'Hotels',
        'show_footer': True
    })