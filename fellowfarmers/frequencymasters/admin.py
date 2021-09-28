from django.contrib import admin
from .models import FrequencyMaster
# Register your models here.

@admin.action(description="Active/Deactive")
def active_deactive(modeladmin,request,queryset):
    for obj in queryset:
        if obj.is_active == True:
            queryset.update(is_active=False)
        else:
            queryset.update(is_active=True)    




@admin.register(FrequencyMaster)
class FrequencyMasterAdmin(admin.ModelAdmin):
    list_display=['label_name','get_products','number_of_days','discount_per','is_active']
    actions=[active_deactive]

    def get_products(self,obj):
        return "\n".join([p.name for p in obj.product.all()])

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions    
