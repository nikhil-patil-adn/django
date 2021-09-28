from django.contrib import admin
from .models import CategoryMaster

# Register your models here.

@admin.register(CategoryMaster)
class CategoryMasterAdmin(admin.ModelAdmin):
    list_display=['name',]


    def has_delete_permission(self, request, obj = None):
        return False     
