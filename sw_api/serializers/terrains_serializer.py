from rest_framework import serializers

from sw_api.models.terrain import Terrain


class TerrainSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Terrain
        fields = [ 'id', 'name' ]
