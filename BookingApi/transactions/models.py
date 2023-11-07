from django.conf import settings
from django.db import models
from promocodes.models import Promocode
from concerts.models import Concert
from django.contrib.auth.models import User

# Create your models here. no!

class Transaction (models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    concert_id = models.ForeignKey(Concert, on_delete=models.CASCADE)
    promocode_id = models.ForeignKey(Promocode, on_delete=models.SET_NULL, null=True)
    data = models.DateField()