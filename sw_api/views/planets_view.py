from rest_framework.views import APIView
from rest_framework.response import Response

from sw_api.models.planet import Planet
from sw_api.serializers.planets_serializer import PlanetSerializer
from sw_api.controllers.planets_controller import PlanetsController


class PlanetsView(APIView):

    def get(self, args):
        planets = PlanetsController().get_all_planets()
        serializer = PlanetSerializer(planets, many=True)
        return Response(serializer.data)

    def post(self, request):
        planet_data = request.data
        planet = PlanetsController().create_planet(planet_data)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)
