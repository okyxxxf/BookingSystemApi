from django.db import models
from .concert import Concert

class OpenAir (models.Model):
    concert_id = models
    directions = models.TextField()
    headliner = models.CharField(max_length=256)