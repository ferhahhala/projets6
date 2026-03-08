from django.contrib import admin # pyright: ignore[reportMissingModuleSource]
from django.urls import path, include # pyright: ignore[reportMissingModuleSource]

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hotels/', include('hotels.urls')),
    path('places/', include('places.urls')),
    path('restaurants/', include('restaurants.urls')),
]