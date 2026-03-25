from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('hotels/', views.hotel_list, name='hotel_list'),         # إضافة
    path('restaurants/', views.restaurant_list, name='restaurant_list'),  # إضافة
    path('fastfood/', views.fastfood_list, name='fastfood_list'),        # إذا لديك view
    path('places/', views.place_list, name='place_list'),         # إضافة
]