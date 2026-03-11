from django.shortcuts import render # type: ignore
from .models import Place

def places_list(request):
    Places = Place.objects.all()
    return render(request, 'places/index_pl.html', {'places': Places})