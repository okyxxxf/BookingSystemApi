from django.shortcuts import render
from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['GET', 'POST'])
def users_list(request):
    users = User.objects.all()

    if request.method == 'GET':
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    