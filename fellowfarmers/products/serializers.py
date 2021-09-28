from products.models import Product
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_photo_url')
    class Meta:
        model=Product
        fields='__all__'

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.image.url
        return request.build_absolute_uri(photo_url) 
