from django.contrib import admin
from .models import Notification
# Register your models here.

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display=['number_of_days_in_advance']

    def number_of_days_in_advance(self,obj):
        return obj.number_of_advance_days_allow

    def has_delete_permission(self, request, obj = None):
        return False     