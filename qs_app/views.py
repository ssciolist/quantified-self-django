from django.shortcuts import render
from django.http import HttpResponse

# imports for jsonification
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
import json

# import to allow some requests without CSRF protection
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from qs_app.models import Food

@csrf_exempt
def food_index(request):
    if request.method == 'GET':
        foods = list(Food.objects.all().values('id', 'name', 'calories'))
        return JsonResponse(foods, safe=False)
    elif request.method == 'POST':
        try:
            food_params = json.loads(request.body)['food']
            food = Food(name = food_params['name'], calories = food_params['calories'])
            food.save()
            return JsonResponse({'id':food.id, 'name':food.name, 'calories':food.calories})
        except:
            return HttpResponse('An error occurred. No food created', status=400)


def food_show(request, food_id):
    if request.method == 'GET':
        food = model_to_dict(Food.objects.get(pk=food_id))
        return JsonResponse(food, safe=False)
    elif request.method == 'POST':
        return HttpResponse('placeholder')
