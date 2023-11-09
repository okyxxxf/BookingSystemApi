from django.db import models

class Concert (models.Model):
    performer = models.CharField(max_length=60)
    tickets_count = models.IntegerField()
    date = models.DateField()
    place = models.CharField(max_length=256)
    price = models.FloatField()
    name = models.CharField(max_length=60)
    description = models.TextField(default='Описание концерта')
    image = models.TextField(default='default.jpg')
    CONCERT_TYPE_CHOICES = [
        ('CM', 'Classical Music'),
        ('OA', 'Open Air'), 
        ('P', 'Party')
    ]
    concert_type = models.CharField(max_length=2, choices=CONCERT_TYPE_CHOICES)