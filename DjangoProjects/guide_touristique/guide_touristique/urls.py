from django.contrib import admin
from django.urls import path, include
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', core_views.home, name='home'),

    # باقي التطبيقات
    path('hotels/', include('hotels.urls')),
    path('places/', include('places.urls')),
    path('restaurants/', include('restaurants.urls')),
]