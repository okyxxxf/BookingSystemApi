from rest_framework import serializers
from concerts.models import Concert

class ConcertSerializer (serializers.ModelSerializer):
    class Meta:
        model = Concert
        fields = [
            'id',
            'performer', 
            'tickets_count', 
            'date', 
            'place', 
            'concert_type'
        ]