from django.shortcuts import render
from django.http import HttpResponse

# imports for jsonification
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

from qs_app.models import Food

def food_index(request):
    foods = list(Food.objects.all().values('id', 'name', 'calories'))
    return JsonResponse(foods, safe=False)

def food_show(request, food_id):
    food = model_to_dict(Food.objects.get(pk=food_id))
    return JsonResponse(food, safe=False)
