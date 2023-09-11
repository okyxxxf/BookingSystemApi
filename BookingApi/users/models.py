from django.db import models

# Create your models here.
class User (models.Model):
    name = models.CharField(max_length=20)
    mail = models.EmailField()
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=5)