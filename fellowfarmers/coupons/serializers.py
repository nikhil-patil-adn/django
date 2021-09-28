from rest_framework import serializers
from .models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model=Coupon
        fields=['id','name','dis_count_per','sales_person','valid_from_date','valid_till_date','order_type',]


