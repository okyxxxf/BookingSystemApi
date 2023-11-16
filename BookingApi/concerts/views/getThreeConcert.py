from rest_framework.decorators import api_view, permission_classes
from concerts.serializers import ConcertSerializer
from concerts.models import Concert
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny 

@api_view(['GET'])
@permission_classes([AllowAny])
def get_three_last(request):
    concerts = Concert.objects.order_by('-id')[0:3]
    serializer = ConcertSerializer(concerts, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
        