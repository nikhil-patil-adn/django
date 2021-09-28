from django.db import models
from customers.models import Customer
from staffpersons.models import StaffPerson

# Create your models here.
class Feedback(models.Model):
    status_choices=(('open','Open'),('in_progress','In Progress'),('closed','Closed'))
    feedback_date=models.DateTimeField(auto_now_add=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)#never put on delete
    type=models.CharField(max_length=200)
    details=models.TextField()
    status=models.CharField(choices=status_choices,max_length=200)
    expected_to_resolved_by=models.ForeignKey(StaffPerson,on_delete=models.CASCADE,null=True)#never put on delete
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)


class FeedbackQuestion(models.Model):
    question=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

