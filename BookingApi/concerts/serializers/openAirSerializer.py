from rest_framework import serializers
from concerts.models import OpenAir

class OpenAirSerializer (serializers.ModelSerializer):
    class Meta:
        model = OpenAir
        fields = [
            'directions',
            'headliner',
            'concert_ptr',
        ]
        depth = 1