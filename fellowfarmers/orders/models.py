from django.db import models
from datetime import datetime
from customers.models import Customer
from staffpersons.models import StaffPerson

# Create your models here.
class Order(models.Model):
    sales=[(i.name,i.name) for i in StaffPerson.objects.filter(designation='sales_person')]
    deliveryguy=[(i.name,i.name) for i in StaffPerson.objects.filter(designation='delivery_guy')]
    ordertypes=[('buynow','Regular'),('subscription','Subscription')]
    status_choices=(('delivery_received','Delivery Received'),('delivery_scheduled','Delivery Scheduled'),
    ('out_for_elivery','Out for Delivery'),('delivered','Delivered'),
    ('cancel','Cancel'))
    order_date=models.DateTimeField(default=datetime.now)
    schedule_delivery_date=models.DateTimeField(default=datetime.now)
    shipping_date=models.DateTimeField(default=datetime.now)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)#never put on delete models cascade
    delivery_address=models.TextField()
    product=models.CharField(max_length=200)
    quantity=models.IntegerField()
    order_type=models.CharField(choices=ordertypes,null=True,max_length=200)
    subscription_type=models.CharField(max_length=200,blank=True,null=True)
    subscription_payment_type=models.CharField(max_length=200,blank=True,null=True)
    prepaid_option=models.CharField(max_length=200,blank=True,null=True)
    order_amount=models.DecimalField(max_digits=6,decimal_places=2,default='00.00')
    sales_person=models.CharField(choices=sales,null=True,max_length=200)
    delivery_staff=models.CharField(choices=deliveryguy,null=True,max_length=200,blank=True)
    tracking_number=models.CharField(max_length=200,default="",null=True,blank=True)
    order_status=models.CharField(choices=status_choices,max_length=200)
    payment_status=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)