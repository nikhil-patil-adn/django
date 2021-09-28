from banners.models import Banner
from django.shortcuts import render
from .models import Banner
from rest_framework import viewsets
from .serializers import BannerSerializer

# Create your views here.


class getBanners(viewsets.ModelViewSet):
    queryset=Banner.objects.all()
    serializer_class=BannerSerializer