from rest_framework import serializers

from sw_api.models.planet import Planet
from sw_api.serializers.climates_serializer import ClimateSerializer
from sw_api.serializers.terrains_serializer import TerrainSerializer


class PlanetSerializer(serializers.ModelSerializer):
    climates = ClimateSerializer(many=True)
    terrains = TerrainSerializer(many=True)
    
    class Meta:
        model = Planet
        fields = [ 'id', 'name', 'population', 'climates', 'terrains' ]
