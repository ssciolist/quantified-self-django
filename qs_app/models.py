from django.db import models

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=200)
    calories = models.IntegerField()

class Meal(models.Model):
    name = models.CharField(max_length=200)

class MealFood(models.Model):
    meal_id: models.ForeignKey(Meal, on_delete=models.CASCADE)
    food_id: models.ForeignKey(Food, on_delete=models.CASCADE)
