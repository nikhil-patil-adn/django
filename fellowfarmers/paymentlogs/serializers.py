from rest_framework import serializers
from .models import Paymentlog


class PaymentlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=Paymentlog
        fields = '__all__'


