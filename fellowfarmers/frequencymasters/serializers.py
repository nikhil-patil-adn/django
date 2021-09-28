from rest_framework import serializers
from .models import FrequencyMaster

class FrequencyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model=FrequencyMaster
        fields='__all__'


