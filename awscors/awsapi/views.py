from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import *
from .serializers import *

# Create your views here.

class userViewserializer(viewsets.ModelViewSet):
    queryset = user.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = userSerializers