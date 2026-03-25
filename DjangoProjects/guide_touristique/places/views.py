from django.shortcuts import render
from .models import Place

def place_list(request):
    wilaya = request.GET.get('wilaya')
    query = request.GET.get('q', '')

    places = Place.objects.all()

    if wilaya:
        places = places.filter(wilaya__icontains=wilaya)

    if query:
        places = places.filter(name__icontains=query)

    return render(request, 'core/list_template.html', {
        'items': places,
        'wilaya': wilaya,
        'query': query,
        'category_name': 'Places',
        'show_footer': True
    })