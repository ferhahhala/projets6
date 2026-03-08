from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.hotel_list, name='hotel_list'),
]