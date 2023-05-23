from rest_framework.views import APIView
from rest_framework.response import Response

from sw_api.models.planet import Planet
from sw_api.controllers.planets_controller import PlanetsController
from sw_api.serializers.planets_serializer import PlanetSerializer


class PlanetDetailsView(APIView):

    def get(self, request, *args, **kwargs):
        planet_id = kwargs.get('planet_id')
        planet = PlanetsController().get_planet_by_id(planet_id)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        planet_id = kwargs.get('planet_id')
        PlanetsController().delete_planet_by_id(planet_id)
        return Response('ok')

    def put(self, request, *args, **kwargs):
        planet_id = kwargs.get('planet_id')
        planet_data = request.data
        planet = PlanetsController().update_planet(planet_id, planet_data)
        serializer = PlanetSerializer(planet)
        return Response(serializer.data)
