from rest_framework.response import Response
from rest_framework.decorators import api_view
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework import status

@api_view(['GET'])
def user_transactions (request, pk):
    user_transactions = Transaction.objects.filter(user_id=pk)
    serializer = TransactionSerializer(user_transactions, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)