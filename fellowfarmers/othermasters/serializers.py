from products.models import Product
from rest_framework import serializers
from .models import CityMaster

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=CityMaster
        fields=['id','code','name','active',]


