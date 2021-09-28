from rest_framework import serializers
from .models import Order
from customers.serializers import CustomerSerializer

class OrderSerializer(serializers.ModelSerializer):
    customer=CustomerSerializer()
    class Meta:
        model=Order
        fields = '__all__'


