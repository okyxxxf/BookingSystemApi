from django.db import models
from users.models import User
from concerts.models import Concert
from promocodes.models import Promocode

# Create your models here. no!

class Transaction (models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    concert_id = models.ForeignKey(Concert, on_delete=models.CASCADE)
    promocode_id = models.ForeignKey(Promocode, on_delete=models.SET_NULL, null=True)
    data = models.DateField()