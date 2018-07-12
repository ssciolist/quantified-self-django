# Quantified Self (Django Edition)

Quantified Self is an API built with Django to serve JSON data meals and snacks to track calories. This API is intended to serve a separate Quantified Self front end, which you can see [deployed here](https://ssciolist.github.io/qs-fe-django/).

See the API itself deployed [on Heroku here](https://fierce-mountain-30405.herokuapp.com/api/v1/foods/).

Check out the API reference index to see everything you can do.

## Setup

*Note*: This projects runs Django 2 and Python 3.7. So you'll need to use pip3 for installing dependencies. 

Once you've forked or cloned this repository to your computer, you should create a virtual environment and activate it.

`python3 -m venv your-env-name
source your-env-name/bin/activate`

Next, install the api's dependencies.

`pip3 install -r requirements/local.txt`

Then, create your PostgreSQL database.

`CREATE DATABASE qs_django;`

Run the migrations with the following command. This will set up the database and seed it with 4 meals; breakfast, lunch, snack and dinner.

`python3 manage.py migrate`

Now you should be able to run `python3 manage.py runserver` to start a server locally and query the API. 

Most server instances will be accessible at http://localhost:8000/. If you're testing interaction with the local front end, I recommend running `python3 manage.py runserver 3000` to ensure your local instance will run from port 3000 -- the front end expects that. 

## Running the tests

Use `python3 manage.py test` from the terminal to run all tests.

## API reference index

This API has 9 endpoints designed to support calorie tracking in the QS front end. Click on one of the endpoints to jump to more information about how to use it.

No API keys or additional header information should be required to access the API.

1. [GET request to "/api/v1/foods"](#Allfoods)
2. [POST request to "/api/v1/foods"](#new_food)
3. [GET request to "/api/v1/foods/:id"](#show_food)
4. [PATCH request to "/api/v1/foods/:id"](#update_food)
5. [DELETE request to "/api/v1/foods/:id"](#delete_food)
6. [GET request to "/api/v1/meals"](#all_meals)
7. [GET request to "/api/v1/meals/:meal_id/foods"](#show_meal)
8. [POST request to "/api/v1/meals/:meal_id/foods/:food_id"](#update_meal_food)
9. [DELETE request to "/api/v1/meals/:meal_id/foods/:food_id"](#delete_meal_food)

#### <a name="Allfoods"></a> GET request to "/api/v1/foods"
A properly formatted API call will return all foods in the database currently.

Each individual food will be returned with an id, name and calories. EG:

```
{
"id": 1,
"name": "Banana",
"calories": 150
}
```
#### <a name="new_food"></a> POST request to "/api/v1/foods"
A properly formatted request to "/api/v1/foods" will create a new food and return that food as JSON formatted with its id, name and calories.

To create a food, you need to send food data in the post body. Follow this format:

```
{ "food": { "name": "Name of food here", "calories": "Calories here"} }
```

#### <a name="show_food"></a> GET request to "/api/v1/foods/:id"
A properly formatted request to "/api/v1/foods/:id" will return an individual food will be returned with an id, name and calories.

To return an individual food, you need to know the ID of the food record and include it in your call.


```
{
"id": 1,
"name": "Banana",
"calories": 150
}
```

#### <a name="update_food"></a> PATCH request to "/api/v1/foods/:id"
A properly formatted request will update an individual food and it will be returned with an id, name and calories.

To update a food, you need to send food data in the post body. Follow this format:

```
{ "food": { "name": "Name of food here", "calories": "Calories here"} }
```

#### <a name="delete_food"></a> DELETE request to "/api/v1/foods/:id"
A properly formatted request will delete an individual food and return a success message.

To update a food, you need to include its id.
#### <a name="all_meals"></a> GET request to "/api/v1/meals"
A properly formatted request will return all meals in the database.

#### <a name="show_meal"></a> GET request to "/api/v1/meals/:meal_id/foods"
A properly formatted request will return all foods of an individual meal in the database.

To call the meal foods, you need to include the id of the meal.

#### <a name="update_meal_food"></a> POST request to "/api/v1/meals/:meal_id/foods/:food_id"
A properly formatted request will add one foods to an individual meal in the database.

A success yields the following message:

```
{
    "message": "Successfully added FOODNAME to MEALNAME"
}
```

#### <a name="delete_meal_food"></a> DELETE request to "/api/v1/meals/:meal_id/foods/:food_id"

A properly formatted request will delete one foods to an individual meal in the database.

A success yields the following message:

```
{
    "message": "Successfully removed FOODNAME from MEALNAME"
}
```


## Versions

* Python version 3.7.0
* PostgreSQL version 10.3
* Django version 2.0
