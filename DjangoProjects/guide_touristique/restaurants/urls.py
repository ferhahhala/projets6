from django.urls import path # pyright: ignore[reportMissingModuleSource]
from . import views

urlpatterns = [
    path('', views.restaurents_list, name='restaurants'),
]