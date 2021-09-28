from django.contrib import admin
from .models import MyHoliday
# Register your models here.

@admin.register(MyHoliday)
class MyHolidayAdmin(admin.ModelAdmin):
    list_display=['id','customer','startdate','enddate',]

    def has_delete_permission(self, request, obj = None):
        return False 