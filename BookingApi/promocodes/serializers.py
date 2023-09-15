from rest_framework import serializers
from promocodes.models import Promocode

class PromocodeSerializer (serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = [
            'id', 
            'code', 
            'discount', 
            'start_date', 
            'end_date'
        ]