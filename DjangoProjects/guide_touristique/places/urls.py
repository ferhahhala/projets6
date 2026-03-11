from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.places_list, name='places'),
    
]