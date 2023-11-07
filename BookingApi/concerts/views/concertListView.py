from rest_framework.decorators import api_view, permission_classes
from concerts.serializers import ConcertSerializer, ClassicMusicSerializer, OpenAirSerializer, PartySerializer
from concerts.models import Concert, ClassicMusic, OpenAir, Party
from rest_framework.response import Response
from .getConcert import get_concert
from rest_framework import status
from .createConcert import create_concert
from rest_framework.permissions import AllowAny

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def concerts_list(request):
    concerts = Concert.objects.all()
    result = []


    if request.method == 'GET':
        for concert in concerts:
            # проверка на тип концерта и последующий запрос к нужной таблице
            match concert.concert_type:
                case 'CM':
                    temp = get_concert(ClassicMusicSerializer, ClassicMusic, concert)
                    result.append(temp)

                case 'OA':
                    temp = get_concert(OpenAirSerializer, OpenAir, concert)
                    result.append(temp)

                case 'P':
                    temp = get_concert(PartySerializer, Party, concert)
                    result.append(temp)        
            

        return Response(result, status=status.HTTP_200_OK)


    if request.method == 'POST':
        concert_type = request.data[0].get('concert_type')
        concert_serializer = ConcertSerializer(data=request.data[0])
        match concert_type:
            case 'CM':
                return create_concert(concert_serializer, request, ClassicMusicSerializer)
            case 'OA':
                return create_concert(concert_serializer, request, OpenAirSerializer)
            case 'P':
                return create_concert(concert_serializer, request, PartySerializer)

        return Response(status=status.HTTP_400_BAD_REQUEST)
        