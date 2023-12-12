from rest_framework.decorators import api_view
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def transaction_details(request, pk):
    try:
        transaction = Transaction.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    match request.method:
        case 'GET':
            serializer = TransactionSerializer(transaction)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        case 'PUT':
            serializer = TransactionSerializer(transaction, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        case 'PATCH':
            serializer = TransactionSerializer(transaction, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(status=status.HTTP_400_BAD_REQUEST)

        case 'DELETE':
            transaction.concert_id.tickets_count += 1
            transaction.delete()

            return Response(status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)