from django.contrib import admin
from .models import Subscription,Postpaid,Prepaid
from django.utils.safestring import mark_safe 

# Register your models here.

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display=['id','subscription_start','subscription_end','customer','subscription_type','frequency_type','sales_person','delivery_guy'] 

    def has_delete_permission(self, request, obj = None):
        return False 

    def delivery_guy(self,obj):
        if obj.delivery_staff == None:
            url="/admin/subscriptions/subscription/{}/change/".format(obj.id)
            return mark_safe('<a href="{}">Allocate</a>'.format(url))
        else:
            return obj.delivery_staff    


@admin.register(Postpaid)
class PostpaidAdmin(admin.ModelAdmin):
    list_display=['number_of_days_advance_notification','negative_balance_allow_for_number_of_day']

    def has_delete_permission(self, request, obj = None):
        return False 

    def number_of_days_advance_notification(self,obj):
        return obj.number_of_advance_days_allow

    def negative_balance_allow_for_number_of_day(self,obj):
        return obj.negative_balance    


@admin.register(Prepaid)
class PrepaidAdmin(admin.ModelAdmin):
    list_display=['number_of_days_advance_notification','negative_balance_allow_for_number_of_day']

    def has_delete_permission(self, request, obj = None):
        return False 

    def number_of_days_advance_notification(self,obj):
        return obj.number_of_advance_days_allow

    def negative_balance_allow_for_number_of_day(self,obj):
        return obj.negative_balance  