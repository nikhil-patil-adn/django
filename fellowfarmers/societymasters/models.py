from django.db import models
from staffpersons.models import StaffPerson

# Create your models here.

class SocietyMaster(models.Model):
    sales=[(i.name,i.name) for i in StaffPerson.objects.filter(designation='sales_person')]
    code=models.IntegerField()
    name=models.CharField(max_length=200)
    assign_sale_person=models.CharField(choices=sales,max_length=200,null=True)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name   