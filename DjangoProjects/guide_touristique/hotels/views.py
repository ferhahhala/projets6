from django.shortcuts import render # type: ignore
from .models import Hotel

def index_hot(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/index_hot.html', {'hotels': hotels})