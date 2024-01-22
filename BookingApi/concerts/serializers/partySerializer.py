from rest_framework import serializers
from concerts.models import Party

class PartySerializer (serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = [
            'age_limit',
            'concert_ptr',
        ]
        depth = 1