from django.db import models
from .concert import Concert

class ClassicMusic (models.Model):
    concert_id = models.ForeignKey(Concert, on_delete=models.CASCADE)
    VOICE_TYPE_CHOICES = [
        ('A', 'Alt'),
        ('T', 'Tenor'),
        ('B', 'Bas')
    ]
    voice_type = models.CharField(max_length=1, choices=VOICE_TYPE_CHOICES)
    name = models.CharField(max_length=256)
    composer = models.CharField(max_length=50)