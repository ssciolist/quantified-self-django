from django.urls import path

from . import views

urlpatterns = [
    path('foods/', views.food_index, name='food_index'),
    path('foods/<int:food_id>/', views.food_show, name='food_show'),
    path('foods/<int:food_id>', views.food_show, name='food_put'),
    path('meals/', views.meal_index, name='meal_index'),
]
