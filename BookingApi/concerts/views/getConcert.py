from rest_framework.serializers import ModelSerializer
from django.db.models import Model
from concerts.serializers import ConcertSerializer

def get_concert (
    serializer : ModelSerializer, 
    Model : Model, 
    concert : Model
):
    
    model_concert = Model.objects.get(concert_id = concert.id)

    return [
        ConcertSerializer(concert).data, 
        serializer(model_concert).data
    ]