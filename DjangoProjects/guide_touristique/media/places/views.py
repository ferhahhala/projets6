from django.shortcuts import render
from .models import Place

def place_list(request):
    wilaya = request.GET.get('wilaya')

    places = Place.objects.all()
    if wilaya:
        places = places.filter(wilaya__icontains=wilaya)

    # لا يوجد سعر للـ places، فقط عرض النتائج
    return render(request, 'core/list_template.html', {
        'items': places,
        'wilaya': wilaya,
        'category_name': 'Places',
        'max_price': None
    })