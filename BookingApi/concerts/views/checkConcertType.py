from concerts.models import Concert, ClassicMusic, OpenAir, Party
from concerts.serializers import ClassicMusicSerializer, OpenAirSerializer, PartySerializer

def check_concert_type(
    concert : Concert
):
    match concert.concert_type:
        case 'CM':
            return ClassicMusic
        case 'OA':
            return OpenAir
        case 'P':
            return Party
        

def check_concert_type_serializer(
        concert : Concert
):
    match concert.concert_type:
        case 'CM':
            return ClassicMusicSerializer
        case 'OA':
            return OpenAirSerializer
        case 'P':
            return PartySerializer