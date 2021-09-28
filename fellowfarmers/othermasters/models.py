from django.db import models
#from staffpersons.models import StaffPerson

# Create your models here.


class CityMaster(models.Model):
    code=models.IntegerField()
    name=models.CharField(max_length=200)
    active=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)


    class Meta:
        ordering=('-created',)

    def __str__(self):
        return self.name

# class SalePerson(models.Model):
#     code=models.IntegerField()
#     name=models.CharField(max_length=200)
#     address=models.TextField()
#     city=models.ForeignKey(CityMaster,on_delete=models.CASCADE) 
#     created=models.DateTimeField(auto_now_add=True,blank=True)
#     updated=models.DateTimeField(auto_now=True,blank=True)

#     def __str__(self):
#         return self.name            