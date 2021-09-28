from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','price','city','society','product_image'] 

    def has_delete_permission(self, request, obj = None):
        return False 

