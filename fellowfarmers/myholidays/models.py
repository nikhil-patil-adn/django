from django.db import models
from customers.models import Customer

# Create your models here.
class MyHoliday(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)#never put on delete
    startdate=models.DateField()
    enddate=models.DateField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name='My Plan'


   

