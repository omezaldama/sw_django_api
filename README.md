# Django Star Wars API Project

This is a Python 3.10 project that can download data from the [Star Wars API](https://swapi-graphql.netlify.app) and save it into a local database (SQLite for simplicity).

## Run the project

Download the repository
```
git clone https://github.com/omezaldama/sw_django_api.git
```
or with SSH:
```
git clone git@github.com:omezaldama/sw_django_api.git
```

Start a virtual environment. For example, on Windows:
```
virtualenv venv
```
On Linux (with virtual env wrapper):
```
mkvirtualenv sw
```

Install dependencies (on Windows):
```
pip install -r requirements.txt
```
On Linux/Mac, you might want to write `pip3` instead.

Run the server:
```
python manage.py runserver
```
This will start the server on port 8000 by default (on Linux/Mac, you might want to write `python3` instead), it will also create the sqlite database file.
Stop the server with Ctrl-C.

Create and run migrations to create the necessary tables:
```
python manage.py makemigrations
python manage.py migrate
```
This will create the tables on the sqlite database.

Run the following command to seed the tables with the data from the Star Wars API:
```
python manage.py seed_planets
```

Now you can run the server again and start using the endpoints. All endpoints have an `api` prefix. The following endpoints are available:
| Method | URL                                             | Description           |
|--------|-------------------------------------------------|-----------------------|
| GET    | `http://localhost:8000/api/planets`             | Get all planets       |
| GET    | `http://localhost:8000/api/planets/{planet_id}` | Get planet by id      |
| POST   | `http://localhost:8000/api/planets`             | Create planet         |
| PATCH  | `http://localhost:8000/api/planets/{planet_id}` | Update planet by id   |
| DELETE | `http://localhost:8000/api/planets/{planet_id}` | Delete planet by id   |

For the POST endpoint, the JSON payload should have the following structure:
```
{
	"name": "another planet",
	"population": 1234,
	"climates": [
		"climate 1",
		"climate 2"
	],
	"terrains": [
		"terrain 1",
		"terrain 2",
		"terrain 3"
	]
}
```
If the climates or terrains do not exist, they will be created. This endpoint is also idempotent, so if you provide a name that already exists, the existing planet will be modified instead.

For the PATCH endpoint, the payload is the same. Only the fields sent will be updated. For example, if you send
```
{
    "population": 5678
}
```
then only the population of the planet specified by the id provided in the path parameter will be updated; its name, terrains and climates will be left unchanged. If a planet with the specified id does not exist, the endpoint will just return an error.
