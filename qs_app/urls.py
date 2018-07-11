from django.urls import path

from . import views

urlpatterns = [
    path('foods/', views.food_index, name='food_index'),
    path('foods/<int:food_id>/', views.food_show, name='food_show'),
    path('foods/<int:food_id>', views.food_show, name='food_put'),
    path('meals/', views.meal_index, name='meal_index'),
    path('meals/<int:meal_id>/', views.meal_show, name='meal_index'),
    path('meals/<int:meal_id>/foods/<int:food_id>', views.meal_food_post_delete, name='meal_food_post_delete'),
]
