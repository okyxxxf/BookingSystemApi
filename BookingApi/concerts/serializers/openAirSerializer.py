from rest_framework import serializers
from concerts.models import OpenAir

class OpenAirSerializer (serializers.ModelSerializer):
    class Meta:
        model = OpenAir
        fields = [
            'id',
            'concert_id',
            'directions',
            'headliner',
        ]