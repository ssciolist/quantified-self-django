from django.shortcuts import render
from django.http import HttpResponse

# imports for jsonification
from django.http import JsonResponse
from django.core import serializers

from qs_app.models import Food

def food_index(request):
    foods = list(Food.objects.all().values('id', 'name', 'calories'))
    return JsonResponse(foods, safe=False)
