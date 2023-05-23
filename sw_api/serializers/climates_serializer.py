from rest_framework import serializers

from sw_api.models.climate import Climate


class ClimateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Climate
        fields = [ 'id', 'name' ]
