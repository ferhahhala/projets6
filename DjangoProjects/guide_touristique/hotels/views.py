from django.shortcuts import render # type: ignore
from .models import Hotel

def hotel_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/hotel_list.html', {'hotels': hotels})