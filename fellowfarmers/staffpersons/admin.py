from django.contrib import admin
from .models import StaffPerson
from deliverystaffroster.models import DeliveryStaffRoster
from django.utils.safestring import mark_safe
# Register your models here.


def apply_attendance(modeladmin, request, queryset):
    for obj in queryset:
        sv=DeliveryStaffRoster(staff=obj,attendace_status='present')
        sv.save()

apply_attendance.short_description = 'Present'

@admin.register(StaffPerson)
class StaffPersonAdmin(admin.ModelAdmin):
    list_display=['name','designation','city','map_society']  
    actions = [apply_attendance, ]  
    list_filter=['designation',]

    def has_delete_permission(self, request, obj = None):
        return False 

    def map_society(self,obj):
        url="/admin/societymasters/societymaster/?assign_sale_person__exact={}".format(obj.name)
        return mark_safe('<a href="{}">map society</a>'.format(url))    


# class DeliveryStaffRosterMaster(StaffPerson):
#     class Meta:
#         proxy=True 



# def apply_attendance(modeladmin, request, queryset):
#     for obj in queryset:
#         sv=DeliveryStaffRoster(staff=obj,attendace_status='present')
#         sv.save()

# apply_attendance.short_description = 'Present'

# class MyStaffAdmin(StaffPersonAdmin):
#     list_display=['name','designation']  
#     actions = [apply_attendance, ] 

#     def get_queryset(self, request):
#         return StaffPerson.objects.all()  


# admin.site.register(DeliveryStaffRosterMaster, MyStaffAdmin)        



