# create a client that will make requests
from django.test import TestCase, Client

client = Client()

from qs_app.models import Food, Meal

import json

class FoodViewsTestClass(TestCase):

    def setUp(self):
        Food.objects.create(name='Croissant', calories='400')
        Food.objects.create(name='Salad', calories='300')

    def test_food_index(self):
        response = client.get('/api/v1/foods/')
        food_list = Food.objects.all().order_by('id')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)[0]['name'], 'Croissant')
        self.assertEqual(json.loads(response.content)[0]['calories'], 400)
        self.assertEqual(json.loads(response.content)[1]['name'], 'Salad')
        self.assertEqual(json.loads(response.content)[1]['calories'], 300)

    def test_valid_food_show(self):
        response = client.get('/api/v1/foods/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], 'Croissant')
        self.assertEqual(json.loads(response.content)['calories'], 400)

    def test_invalid_food_show(self):
        response = client.get('/api/v1/foods/999/')

        self.assertEqual(response.status_code, 404)


    def test_valid_food_post(self):
        payload = '{ "food": { "name": "Tomato Pound Cake", "calories": "900"} }'

        response = client.post('/api/v1/foods/', payload, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], "Tomato Pound Cake")
        self.assertEqual(json.loads(response.content)['calories'], '900')

    def test_invalid_food_post(self):
        payload = '{ "food": { "calories": "900"} }'

        response = client.post('/api/v1/foods/', payload, format='json')

        self.assertEqual(response.status_code, 400)

    def test_valid_food_update(self):
        payload = '{ "food": { "name": "Giant salad", "calories": "500"} }'

        response = client.patch('/api/v1/foods/1/', payload, format='json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], 'Giant salad')
        self.assertEqual(json.loads(response.content)['calories'], '500')

    def test_invalid_food_update(self):
        payload = '{ "food": { "name": "Giant salad" } }'

        response = client.patch('/api/v1/foods/1/', payload, format='json')

        self.assertEqual(response.status_code, 400)

    def test_valid_food_delete(self):
        response = client.delete('/api/v1/foods/2/')

        self.assertEqual(response.status_code, 204)

    def test_invalid_food_delete(self):
        response = client.delete('/api/v1/foods/5/')

        self.assertEqual(response.status_code, 404)

class MealViewsTestClass(TestCase):

    def setUp(self):
        smoothie = Food.objects.create(name='Smoothie', calories='200')
        roll = Food.objects.create(name='Croissant', calories='400')
        salad = Food.objects.create(name='Salad', calories='300')
        chicken = Food.objects.create(name='Whole Roasted Chicken', calories='800')

        Meal.objects.get(name="Breakfast").foods.add(smoothie)
        Meal.objects.get(name="Lunch").foods.add(salad)
        Meal.objects.get(name="Snack").foods.add(roll)
        Meal.objects.get(name="Dinner").foods.add(chicken)

    def test_meal_index(self):
        response = client.get('/api/v1/meals/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)[0]['name'], 'Breakfast')
        self.assertEqual(json.loads(response.content)[0]['foods'][0]['name'], 'Smoothie')
        self.assertEqual(json.loads(response.content)[0]['foods'][0]['calories'], 200)

    def test_valid_meal_show(self):
        response = client.get('/api/v1/meals/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['name'], 'Breakfast')
        self.assertEqual(json.loads(response.content)['foods'][0]['name'], 'Smoothie')
        self.assertEqual(json.loads(response.content)['foods'][0]['calories'], 200)

    def test_invalid_meal_show(self):
        response = client.get('/api/v1/meals/10/')

        self.assertEqual(response.status_code, 404)

    def test_valid_meal_food_post(self):
        response = client.post('/api/v1/meals/1/foods/2')

        self.assertEqual(json.loads(response.content)['message'], 'Successfully added Croissant to Breakfast')

    # def test_invalid_meal_food_post(self):
    #     response = client.post('/api/v1/meals/6/foods/2')
    #
    #     self.assertEqual(response.status_code, 404)
    #
    # def test_invalid_meal_with_invalid_food_post(self):
    #     response = client.post('/api/v1/meals/1/foods/6')
    #
    #     self.assertEqual(response.status_code, 404)
