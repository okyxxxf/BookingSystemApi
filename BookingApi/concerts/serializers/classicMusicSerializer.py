from rest_framework import serializers
from concerts.models import ClassicMusic

class ClassicMusicSerializer (serializers.ModelSerializer):
    class Meta:
        model = ClassicMusic
        fields = [
            'id', 
            'concert_id', 
            'voice_type', 
            'name', 
            'composer'
        ]