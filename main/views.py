from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import FilmSerializers, GenreSerializers


# Create your views here.



class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    permission_classes = [AllowAny, ]


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    permission_classes = [AllowAny, ]

