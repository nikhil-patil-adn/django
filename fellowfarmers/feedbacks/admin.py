from django.contrib import admin
from .models import Feedback, FeedbackQuestion
from django.utils.safestring import mark_safe  
# Register your models here.
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display=['customer','feedback_date','type','details','status','expected_to_resolved_by','action']

    def has_delete_permission(self, request, obj = None):
        return False 

    def action(self,obj):
        updatestatus="/admin/feedbacks/feedback/{}/change/".format(obj.id)
        assignstaff="/admin/feedbacks/feedback/{}/change/".format(obj.id)
        return mark_safe('<a href="{}">Update Status</a> | <a href="{}">Assign Staff</a>'.format(updatestatus,assignstaff))
        

@admin.register(FeedbackQuestion)
class FeedbackQuestionAdmin(admin.ModelAdmin):
    list_display=['question',]    

    # def has_delete_permission(self, request, obj = None):
    #     return False 


  