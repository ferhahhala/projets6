from django.shortcuts import render # type: ignore
from .models import Place

def index_pl(request):
    Places = Place.objects.all()
    return render(request, 'places/index_pl.html', {'places': Places})