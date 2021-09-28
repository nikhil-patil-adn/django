from rest_framework import serializers
from .models import MyHoliday

class MyHolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model=MyHoliday
        fields='__all__'


