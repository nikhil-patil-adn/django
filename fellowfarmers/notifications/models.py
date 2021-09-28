from django.db import models

# Create your models here.


class Notification(models.Model):
    number_of_advance_days_allow=models.IntegerField()
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)