from django.db import models
from othermasters.models import CityMaster
from societymasters.models import SocietyMaster
from products.models import Product
from django.utils.html import mark_safe


# Create your models here.


class Customer(models.Model):
    name=models.CharField(max_length=200)
    username=models.CharField(max_length=200,default="")
    password=models.CharField(max_length=200,default="")
    email=models.CharField(max_length=200)
    mobile=models.CharField(max_length=15)
    address=models.TextField()
    society=models.ForeignKey(SocietyMaster,on_delete=models.CASCADE,null=True)
    city=models.ForeignKey(CityMaster,on_delete=models.CASCADE)
    pincode=models.IntegerField(blank=True,null=True)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name

    def pencil(self):
        return "/images/pencil.png"

class Favourite(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.DO_NOTHING)
    product=models.OneToOneField(Product,on_delete=models.DO_NOTHING)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)
