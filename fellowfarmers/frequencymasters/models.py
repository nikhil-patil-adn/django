from django.db import models
from products.models import Product

# Create your models here.
class FrequencyMaster(models.Model):
    product=models.ManyToManyField(Product)#never put on delete
    label_name=models.CharField(max_length=200)
    number_of_days=models.CharField(max_length=200)
    discount_per=models.CharField(max_length=200,default='0')
    is_active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)
