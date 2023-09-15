from rest_framework.decorators import api_view
from concerts.serializers import ConcertSerializer, ClassicMusicSerializer, OpenAirSerializer, PartySerializer
from concerts.models import Concert, ClassicMusic, OpenAir, Party
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from .checkConcertType import check_concert_type, check_concert_type_serializer

@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def concert_details(request, pk):
    try:
        concert = Concert.objects.get(pk=pk)
        serializer_type = check_concert_type_serializer(concert)
        addition_concert_model = check_concert_type(concert)
        addition_concert = addition_concert_model.objects.get(concert_id = pk)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    match request.method:
        case 'GET':
            serializer = serializer_type(addition_concert)
            concert_serializer = ConcertSerializer(concert)

            return Response([concert_serializer.data, serializer.data], status=status.HTTP_200_OK)
        
        case 'PUT':
            serializer = serializer_type(addition_concert, data=request.data[1])
            concert_serializer = ConcertSerializer(concert, data=request.data[0])
            with transaction.atomic():
                if concert_serializer.is_valid():
                    concert_serializer.save()
                else:
                    transaction.set_rollback(True)

                if serializer.is_valid():
                    serializer.save()
                    return Response([concert_serializer.data, serializer.data], status=status.HTTP_202_ACCEPTED)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        case 'PATCH':
            serializer = serializer_type(addition_concert, data=request.data[1], partial=True)
            concert_serializer = ConcertSerializer(concert, data=request.data[0], partial=True)
            with transaction.atomic():
                if concert_serializer.is_valid():
                    concert_serializer.save()
                else:
                    transaction.set_rollback(True)

                if serializer.is_valid():
                    serializer.save()
                    return Response([concert_serializer.data, serializer.data], status=status.HTTP_202_ACCEPTED)

            return Response(status=status.HTTP_400_BAD_REQUEST)

        case 'DELETE':
            addition_concert = addition_concert_model.objects.get(concert_id = pk)
            with transaction.atomic():
                try:
                    addition_concert.delete()
                    concert.delete()
                except:
                    transaction.set_rollback(True)

            return Response(status=status.HTTP_202_ACCEPTED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)