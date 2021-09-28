from django.db import models
from othermasters.models import CityMaster
from django.core.validators import MaxValueValidator

# Create your models here.


class StaffPerson(models.Model):
    DESIGNATIONS_CHOICES=(
        ('sales_person','Sales Person'),
        ('delivery_guy','Delivery Guy'),
        )
    code=models.IntegerField()
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    username=models.CharField(max_length=200,default='')
    password=models.CharField(max_length=200,default='')
    mobile=models.CharField(max_length=15,null=True)
    address=models.TextField()
    designation=models.CharField(choices=DESIGNATIONS_CHOICES,max_length=20)
    city=models.ForeignKey(CityMaster,on_delete=models.CASCADE)
    pincode=models.PositiveIntegerField(null=True,validators=[MaxValueValidator(999999)])
    #date_of_joining=models.DateTimeField(auto_now_add=True,blank=True) 
    #birthdate=models.DateTimeField(auto_now_add=True,blank=True) 
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.name  