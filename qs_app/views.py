from django.shortcuts import render
from django.http import HttpResponse

# imports for jsonification
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json

# import to allow some requests without CSRF protection
from django.views.decorators.csrf import csrf_exempt, csrf_protect

# import for error handling
from django.shortcuts import get_object_or_404
from qs_app.models import Food, Meal


@csrf_exempt
def food_index(request):
    if request.method == 'GET':
        foods = list(Food.objects.all().values('id', 'name', 'calories'))
        return JsonResponse(foods, safe=False)
    elif request.method == 'POST':
        try:
            food_attrs = json.loads(request.body)['food']
            food = Food(name = food_attrs['name'], calories = food_attrs['calories'])
            food.save()
            return JsonResponse({'id':food.id, 'name':food.name, 'calories':food.calories})
        except:
            return HttpResponse('An error occurred. No food created', status=400)

@csrf_exempt
def food_show(request, food_id):
    if request.method == 'GET':
        food = model_to_dict(get_object_or_404(Food, pk=food_id))
        return JsonResponse(food, safe=False)
    elif request.method == 'PUT' or request.method == 'PATCH':
        try:
            food = get_object_or_404(Food, pk=food_id)

            food.name = json.loads(request.body)['food']['name']
            food.calories = json.loads(request.body)['food']['calories']
            food.save()

            return JsonResponse({'id':food.id, 'name':food.name, 'calories':food.calories})
        except:
            return HttpResponse('An error occurred. No food created', status=400)
    elif request.method == 'DELETE':
        food = get_object_or_404(Food, pk=food_id)
        food.delete()
        return HttpResponse(status=204)

def meal_index(request):
    meals = list(Meal.objects.all().values('id', 'name', 'foods'))
    return JsonResponse(meals, safe=False)

def meal_show(request, meal_id):
    meal = get_object_or_404(Meal, pk=meal_id)
    food_list = list(meal.foods.values('id', 'name', 'calories'))
    return JsonResponse({'id':meal.id, 'name':meal.name, 'foods':food_list})
