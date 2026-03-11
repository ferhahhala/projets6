from django.urls import path # pyright: ignore[reportMissingModuleSource]
from . import views

urlpatterns = [
    path('', views.restaurant_list, name='restaurants'),
]