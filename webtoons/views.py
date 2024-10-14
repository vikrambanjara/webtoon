from django.shortcuts import render

# Create your views here.
# webtoons/views.py
from rest_framework import generics
from .models import Webtoon
from .serializers import WebtoonSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication # type: ignore

class WebtoonListCreate(generics.ListCreateAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    
class WebtoonDetail(generics.RetrieveDestroyAPIView):
    queryset = Webtoon.objects.all()
    serializer_class = WebtoonSerializer
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
