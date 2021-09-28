from rest_framework import serializers
from .models import Subscription
from products.serializers import ProductSerializer

class SubscriptionSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model=Subscription
        fields = '__all__'


