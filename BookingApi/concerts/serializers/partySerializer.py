from rest_framework import serializers
from concerts.models import Party

class PartySerializer (serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = [
            'id',
            'concert_id',
            'age_limit',
        ]