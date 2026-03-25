from django.shortcuts import render
from .models import Hotel

def hotel_list(request):
    wilaya = request.GET.get('wilaya')
    query = request.GET.get('q','')   # 🔥 هذا الجديد

    hotels = Hotel.objects.all()

    # فلترة بالولاية
    if wilaya:
        hotels = hotels.filter(wilaya__icontains=wilaya)

    # 🔥 فلترة بالاسم (search)
    if query:
     hotels = hotels.filter(name__icontains=query)

    # ترتيب حسب السعر
    hotels = hotels.order_by('price')

    return render(request, 'core/list_template.html', {
        'items': hotels,
        'wilaya': wilaya,
        'query': query,   # 🔥 مهم باش يبقى مكتوب في input
        'category_name': 'Hotels',
        'max_price': None,
        'show_footer': True
    })