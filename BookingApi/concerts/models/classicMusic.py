from django.db import models
from .concert import Concert

class ClassicMusic (Concert):
    concert_ptr = models.OneToOneField(
        Concert,
        on_delete=models.CASCADE,
        parent_link=True,
    )
    VOICE_TYPE_CHOICES = [
        ('A', 'Alt'),
        ('T', 'Tenor'),
        ('B', 'Bas')
    ]
    voice_type = models.CharField(max_length=1, choices=VOICE_TYPE_CHOICES)
    composer = models.CharField(max_length=50)