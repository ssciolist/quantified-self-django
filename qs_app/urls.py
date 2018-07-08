from django.urls import path

from . import views

urlpatterns = [
    path('foods/', views.food_index, name='index'),
    path('foods/<int:food_id>/', views.food_show, name='show'),
]
