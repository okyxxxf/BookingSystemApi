from rest_framework import serializers
from concerts.models import ClassicMusic

class ClassicMusicSerializer (serializers.ModelSerializer):
    class Meta:
        model = ClassicMusic
        fields = [
            'voice_type', 
            'composer',
            'concert_ptr',
        ]
        depth = 1