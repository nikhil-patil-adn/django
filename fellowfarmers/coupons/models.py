from django.db import models
from staffpersons.models import StaffPerson

# Create your models here.

class Coupon(models.Model):
    sales=[(i.name,i.name) for i in StaffPerson.objects.filter(designation='sales_person')]
    ordertypes=[('buynow','Buy Now')]
    name=models.CharField(max_length=200)
    sales_person=models.CharField(choices=sales,blank=True,default=None,max_length=200)
    valid_from_date=models.DateTimeField(auto_now_add=True)
    valid_till_date=models.DateTimeField(auto_now_add=True)
    order_type=models.CharField(choices=ordertypes,max_length=200)
    dis_count_per=models.IntegerField(default=0)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name