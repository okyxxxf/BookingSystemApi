from django.db import models

# Create your models here.
class Promocode (models.Model):
    code = models.CharField(max_length=20)
    discount = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()