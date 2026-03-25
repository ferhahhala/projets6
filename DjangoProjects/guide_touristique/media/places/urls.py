from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.place_list, name='place_list'),
    
]