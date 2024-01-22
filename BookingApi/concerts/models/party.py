from django.db import models
from .concert import Concert

class Party (Concert):
    concert_ptr = models.OneToOneField(
        Concert,
        on_delete=models.CASCADE,
        parent_link=True,
    )
    age_limit = models.IntegerField()