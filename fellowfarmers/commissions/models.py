from django.db import models
from staffpersons.models import StaffPerson
from orders.models import Order

# Create your models here.

class SalePersonCommission(models.Model):
    sale_person_choices=[(i.name,i.name) for i in StaffPerson.objects.filter(designation='sales_person')]
    ststus_choices=(('unpaid','Un-Paid'),('paid','Paid'))
    sale_person=models.CharField(choices=sale_person_choices,max_length=200)
    commission_percentage=models.IntegerField()
    status=models.CharField(choices=ststus_choices,max_length=200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sale_person

class CommissionLog(models.Model):
    # sales_person = models.CharField(max_length=200)
    # order_date = models.DateTimeField()
    # commission_amt = models.PositiveIntegerField(default=0)
    # commission_percentage = models.IntegerField()
    sales_person = models.ForeignKey(Order, on_delete=models.CASCADE)
    commission_percentage = models.ForeignKey(SalePersonCommission, on_delete=models.CASCADE)
    commission_amt = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.sales_person)        