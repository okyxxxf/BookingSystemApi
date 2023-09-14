from django.db import models
from .concert import Concert
class OpenAir (models.Model):
    concert_id = models.ForeignKey(Concert, on_delete=models.CASCADE)
    directions = models.TextField()
    headliner = models.CharField(max_length=256)