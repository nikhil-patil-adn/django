
from django.contrib import admin
from .models import SalePersonCommission, CommissionLog

from django.utils.html import format_html
from django.urls import reverse

# Register your models here.
@admin.register(SalePersonCommission)
class SalePersonCommissionAdmin(admin.ModelAdmin):
    list_display=['sale_person','commission_percentage','status']

    def has_delete_permission(self, request, obj = None):
        return False  

@admin.register(CommissionLog)
class CommissionLogAdmin(admin.ModelAdmin):
    list_display=['sales_person', 'order_date', 'order_amount','commission_amt', 'commission_percentage', 'payment']

    @admin.display()
    def order_date(self, obj):
        return (obj.sales_person.order_date)

    @admin.display()
    def order_amount(self, obj):
        return (obj.sales_person.order_amount)

    def has_delete_permission(self, request, obj = None):
        return False      


    @admin.display()
    def payment(self, obj):
        return format_html(
            '<a class="button" href="{}">Pay Now</a>', reverse('commission-pay', args=[obj.id]),
        )

