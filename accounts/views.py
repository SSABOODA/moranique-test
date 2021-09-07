
from django.shortcuts import render
from rest_framework import generics, serializers

from .models import User
from .serializers import UserSerializer


class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDelete(generics.RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
