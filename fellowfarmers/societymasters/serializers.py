from products.models import Product
from rest_framework import serializers
from .models import SocietyMaster

class SocietySerializer(serializers.ModelSerializer):
    class Meta:
        model=SocietyMaster
        fields='__all__'


