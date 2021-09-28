from django.contrib import admin
from .models import Coupon
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display=['name','dis_count_per','valid_from_date','valid_till_date','sales_person']

    def has_delete_permission(self, request, obj = None):
        return False  


