from promocodes.models import Promocode
from promocodes.serializers import PromocodeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def promocodes_list(request):
    promocodes = Promocode.objects.all()

    match request.method:
        case 'GET':
            serializer = PromocodeSerializer(promocodes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        case 'POST':
            serializer = PromocodeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def promocodes_details(request, pk):
    promocode = Promocode.objects.get(pk=pk)

    match request.method:
        case 'GET':
            serializer = PromocodeSerializer(promocode)
            return Response(serializer.data, status=status.HTTP_200_OK)

        case 'PUT':
            serializer = PromocodeSerializer(promocode, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        case 'PATCH':
            serializer = PromocodeSerializer(promocode, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        case 'DELETE':
            promocode.delete()
            return Response(status=status.HTTP_200_OK)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)