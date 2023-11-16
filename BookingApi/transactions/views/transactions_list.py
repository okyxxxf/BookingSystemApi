from rest_framework.decorators import api_view
from transactions.models import Transaction
from transactions.serializers import TransactionSerializer
from rest_framework.response import Response
from rest_framework import status
from concerts.models import Concert

@api_view(['GET', 'POST'])
def transactions_list(request):
    transactions = Transaction.objects.all()
    
    match request.method:
        case 'GET':
            serializer = TransactionSerializer(transactions, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)
            
        case 'POST':
            serializer = TransactionSerializer(data=request.data)
            concert = Concert.objects.get(id=request.data['concert_id'])
            if concert.tickets_count < 1: 
                return Response(status=status.HTTP_400_BAD_REQUEST)
            concert.tickets_count -= 1
            concert.save()   

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)
            