from products.models import Product
from customers.models import Customer
from django.db import models
from datetime import datetime
from customers.models import Customer
from staffpersons.models import StaffPerson
# Create your models here.

class Subscription(models.Model):
    sales=[(i.name,i.name) for i in StaffPerson.objects.filter(designation='sales_person')]
    deliveryguy=[(i.name,i.name) for i in StaffPerson.objects.filter(designation='delivery_guy')]
    sub_choices=(('prepaid','Prepaid'),('postpaid','Postpaid'))

    subscription_date=models.DateTimeField(default=datetime.now)
    subscription_start=models.DateTimeField(default=datetime.now)
    subscription_end=models.DateTimeField(default=datetime.now)
    subscription_renewal_date=models.DateTimeField(blank=True,null=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='cust')
    delivery_address=models.TextField()
    product=models.ForeignKey(Product,on_delete=models.CASCADE,default=1,related_name='prd')
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=6,decimal_places=2,default='00.00')
    subscription_type=models.CharField(choices=sub_choices,max_length=200,default='prepaid')
    frequency_type=models.CharField(max_length=200,default='1')
    sales_person=models.CharField(choices=sales,max_length=200,null=True,blank=True)
    delivery_staff=models.CharField(choices=deliveryguy,max_length=200,null=True,blank=True)
    status=models.CharField(max_length=200)
    resume_subscription=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


class Postpaid(models.Model):
    number_of_advance_days_allow=models.IntegerField()
    negative_balance=models.DecimalField(max_digits=6,decimal_places=2,default='00.00')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


class Prepaid(models.Model):
    number_of_advance_days_allow=models.IntegerField()
    negative_balance=models.DecimalField(max_digits=6,decimal_places=2,default='00.00')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


