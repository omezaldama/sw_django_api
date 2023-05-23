from django.core.management.base import BaseCommand, CommandError

from python_graphql_client import GraphqlClient

from sw_api.controllers.planets_controller import PlanetsController


query = 'query Query {allPlanets{planets{name population terrains climates}}}'

class Command(BaseCommand):
    help = "Fetches planets from the Star Wars Api and saves them into the database"

    def __init__(self, *args, **kwargs):
        self.client = GraphqlClient(endpoint='https://swapi-graphql.netlify.app/.netlify/functions/index')

    def handle(self, *args, **options):
        response = self.client.execute(query=query)
        planets_data = response.get('data').get('allPlanets').get('planets')
        planets_controller = PlanetsController()
        for planet_data in planets_data:
            planets_controller.create_planet(planet_data)
