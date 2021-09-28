from rest_framework import serializers
from .models import StaffPerson

class StaffPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffPerson
        fields='__all__'


