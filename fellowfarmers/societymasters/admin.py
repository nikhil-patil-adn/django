from django.contrib import admin
from .models import SocietyMaster
# Register your models here.



def apply_active(modeladmin, request, queryset):
    for obj in queryset:
        print(obj.active)
        if obj.active == True:
            newactive=False
        else:
            newactive=True    
        SocietyMaster.objects.filter(pk=obj.id).update(active=newactive)

apply_active.short_description = 'Active/Deactive'


@admin.register(SocietyMaster)
class SocietyMasterAdmin(admin.ModelAdmin):
    list_display=['code','name','assign_sale_person','active'] 
    list_filter=['assign_sale_person',]
    actions=[apply_active,]

    def has_delete_permission(self, request, obj = None):
        return False 
