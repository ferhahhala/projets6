from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # الصفحة الرئيسية
    path('', core_views.home, name='home'),

    # صفحة الكاتيجوريز بعد اختيار الولاية
    path('categories/', core_views.categories, name='categories'),

    # باقي التطبيقات
    path('hotels/', include('hotels.urls')),
    path('places/', include('places.urls')),
    path('restaurants/', include('restaurants.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)