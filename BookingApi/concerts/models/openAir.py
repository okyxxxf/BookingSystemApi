from django.db import models
from .concert import Concert
class OpenAir (Concert):
    concert_ptr = models.OneToOneField(
        Concert,
        on_delete=models.CASCADE,
        parent_link=True,
    )
    directions = models.TextField()
    headliner = models.CharField(max_length=256)