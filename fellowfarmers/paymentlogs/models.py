from django.db import models
from django.db.models.fields import CharField
from customers.models import Customer
# Create your models here.


class Paymentlog(models.Model):
    ordertypes=[('buynow','Regular'),('subscription','Subscription')]
    order_type=models.CharField(choices=ordertypes,max_length=200)
    order_id=models.CharField(max_length=200)
    transaction_id=models.CharField(max_length=200)
    paymentdate=models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=6,decimal_places=2,default='00.00')
    customerid=models.ForeignKey(Customer,on_delete=models.DO_NOTHING,default="")
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
