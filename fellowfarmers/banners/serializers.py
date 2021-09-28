from .models import Banner
from rest_framework import serializers


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields=['banner']
