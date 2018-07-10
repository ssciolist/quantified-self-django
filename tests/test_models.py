from django.test import TestCase
from qs_app.models import Food, Meal

class FoodTestClass(TestCase):

    def setUp(self):
        Food.objects.create(name="Croissant", calories='400')
        Food.objects.create(name="Salad", calories='300')

    def test_food_attrs(self):
        buttery_goodness = Food.objects.get(name="Croissant")
        salad = Food.objects.get(name="Salad")

        self.assertEqual(buttery_goodness.calories, 400)
        self.assertEqual(salad.calories, 300)

class MealTestClass(TestCase):

    def setUp(self):
        Food.objects.create(name="Croissant", calories='400')
        Food.objects.create(name="Salad", calories='300')

    def test_meal_food_relation(self):
        roll = Food.objects.get(name="Croissant")
        salad = Food.objects.get(name="Salad")
        breakfast = Meal.objects.get(name="Breakfast")
        lunch = Meal.objects.get(name="Lunch")

        breakfast.foods.add(roll)
        lunch.foods.add(roll, salad)

        self.assertEqual(breakfast.foods.count(), 1)
        self.assertEqual(lunch.foods.count(), 2)
        self.assertQuerysetEqual(breakfast.foods.all(), [f'{roll}'], transform=str)
        self.assertQuerysetEqual(lunch.foods.all().order_by('id'), [f'{roll}', f'{salad}'], transform=str, ordered=True)
