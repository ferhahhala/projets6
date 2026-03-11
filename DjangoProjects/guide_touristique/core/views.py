from django.shortcuts import render, redirect
from .models import Wilaya, Category

def home(request):
    wilayas = Wilaya.objects.all()
    categories = Category.objects.all()

    if request.method == 'POST':
        wilaya_id = request.POST.get('wilaya')
        category_id = request.POST.get('category')

        wilaya = Wilaya.objects.get(id=wilaya_id)
        category = Category.objects.get(id=category_id)

        # تحويل الاسم إلى lowercase للـ URL
        return redirect(f'/{category.name.lower()}/?wilaya={wilaya.name}')

    return render(request, 'core/home.html', {'wilayas': wilayas, 'categories': categories})