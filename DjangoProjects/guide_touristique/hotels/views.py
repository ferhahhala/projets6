from django.shortcuts import render # type: ignore
from .models import Hotel

def hotels_list(request):
    hotels = Hotel.objects.all()
    return render(request, 'hotels/index_hot.html', {'hotels': hotels})