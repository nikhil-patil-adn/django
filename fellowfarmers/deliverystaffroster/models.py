from staffpersons.models import StaffPerson
from django.db import models
# Create your models here.


class DeliveryStaffRoster(models.Model):
    attendacestatus=[('present','Present'),('absent','Absent')]
    staff=models.ForeignKey(StaffPerson,on_delete=models.CASCADE)
    attendace_status=models.CharField(choices=attendacestatus,max_length=200)
    date_of_attendance=models.DateTimeField(auto_now_add=True)
    created=models.DateTimeField(auto_now_add=True,blank=True)
    updated=models.DateTimeField(auto_now=True,blank=True)

    def __str__(self):
        return self.attendace_status