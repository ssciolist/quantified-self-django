# create a client that will make requests
from django.test import TestCase, Client
client = Client()

from qs_app.models import Food, Meal

import json

class FoodViewsTestClass(TestCase):

    def setUp(self):
        Food.objects.create(name="Croissant", calories='400')
        Food.objects.create(name="Salad", calories='300')

    def test_food_index(self):
        response = client.get('/api/v1/foods')
        food_list = Food.objects.all().order_by('id')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)[0]['name'], "Croissant")
        self.assertEqual(json.loads(response.content)[0]['calories'], 400)
        self.assertEqual(json.loads(response.content)[1]['name'], "Salad")
        self.assertEqual(json.loads(response.content)[1]['calories'], 300)
