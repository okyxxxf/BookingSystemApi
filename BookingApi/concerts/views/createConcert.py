from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from rest_framework.serializers import ModelSerializer

def create_concert (
    concert_serializer : ModelSerializer,
    request : dict,
    model_serializer : ModelSerializer,
):
    with transaction.atomic():
        if concert_serializer.is_valid():
            concert_serializer.save()
            id = concert_serializer.data['id']
        else:
            return Response(concert_serializer.errors,status=status.HTTP_401_UNAUTHORIZED)
                    
        request.data[1]['concert_id'] = id
        serializer = model_serializer(data=request.data[1])

        if serializer.is_valid():
            serializer.save()
        else:
            transaction.set_rollback(True)
            return Response(status=status.HTTP_400_BAD_REQUEST)
                    
    return Response([concert_serializer.data, serializer.data], status=status.HTTP_201_CREATED)