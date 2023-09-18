from rest_framework import serializers
from transactions.models import Transaction

class TransactionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id',
            'user_id',
            'concert_id',
            'promocode_id',
            'data'
        ]