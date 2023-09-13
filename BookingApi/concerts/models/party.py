from django.db import models
from .concert import Concert

class Party (models.Model):
    concert_id = models.ForeignKey(Concert, on_delete=models.CASCADE)
    age_limit = models.IntegerField()