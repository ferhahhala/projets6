from django.shortcuts import render, redirect
from .models import Wilaya

def home(request):
    wilayas = Wilaya.objects.all()

    if request.method == 'POST':
        wilaya_id = request.POST.get('wilaya')
        wilaya = Wilaya.objects.get(id=wilaya_id)
        return redirect(f'/categories/?wilaya={wilaya.name}')

    return render(request, 'core/home.html', {'wilayas': wilayas,'show_footer': False})


def categories(request):
    wilaya = request.GET.get('wilaya')

    if request.method == 'POST':
        category = request.POST.get('category')

        if category == 'fastfood':
            return redirect(f'/restaurants/?wilaya={wilaya}&type=fastfood')

        elif category == 'restaurants':
            return redirect(f'/restaurants/?wilaya={wilaya}&type=restaurant')

        elif category == 'hotels':
            return redirect(f'/hotels/?wilaya={wilaya}')

        elif category == 'places':
            return redirect(f'/places/?wilaya={wilaya}')

    return render(request, 'core/categories.html', {
        'wilaya': wilaya,
        'show_footer': False
    })