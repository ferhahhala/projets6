from django.shortcuts import render
from .models import Hotel

def hotel_list(request):
    wilaya = request.GET.get('wilaya')

    hotels = Hotel.objects.all()
    if wilaya:
        hotels = hotels.filter(wilaya__icontains=wilaya)

    # ترتيب تلقائي حسب السعر تصاعديًا
    hotels = hotels.order_by('price')

    return render(request, 'core/list_template.html', {
        'items': hotels,
        'wilaya': wilaya,
        'category_name': 'Hotels',
        'max_price': None
    })