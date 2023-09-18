from rest_framework.decorators import api_view
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def transactions_list(request):
    transactions = Transaction.objects.all()
    
    match request.method:
        case 'GET':
            serializer = TransactionSerializer(transactions, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        case 'POST':
            serializer = TransactionSerializer(data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)
            