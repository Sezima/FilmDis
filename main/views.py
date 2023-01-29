from django.shortcuts import render

from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import FilmSerializers, GenreSerializers
from django_filters.rest_framework import  DjangoFilterBackend




# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def mypage(request):
    return render(request, 'general.html', {})


class GenreViewSet(viewsets.ModelViewSet):
    """For crud genre"""
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    permission_classes = [AllowAny, ]



class FilmViewSet(viewsets.ModelViewSet):
    """For crud model film"""
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    permission_classes = [AllowAny, ]
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['title', 'tag', 'year']



class Search(generics.ListAPIView):
    """Поиск"""
    queryset = Film.objects.all()
    serializer_class = FilmSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title', 'tag']

