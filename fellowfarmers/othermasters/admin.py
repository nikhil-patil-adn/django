from django.contrib import admin
from .models import CityMaster
# Register your models here.



def apply_active(modeladmin, request, queryset):
    for obj in queryset:
        print(obj.active)
        if obj.active == True:
            newactive=False
        else:
            newactive=True    
        CityMaster.objects.filter(pk=obj.id).update(active=newactive)

apply_active.short_description = 'Active/Deactive'

@admin.register(CityMaster)
class CityMasterAdmin(admin.ModelAdmin):
    list_display=['code','name','active']
    actions=[apply_active,]

    def has_delete_permission(self, request, obj = None):
        return False 
    


# @admin.register(SalePerson)
# class SalePersonAdmin(admin.ModelAdmin):
#     list_display=['code','name','city']
       


