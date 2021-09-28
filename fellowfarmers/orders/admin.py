from django.contrib import admin
from .models import Order
from django.utils.safestring import mark_safe 
from datetime import timedelta,datetime
from rangefilter.filters import DateRangeFilter
from staffpersons.models import StaffPerson
# Register your models here.

# for i in StaffPerson.objects.filter(designation='delivery_guy'):
#     print(i)
#     @admin.action(description=i.name)
#     def allocate_staff(modeladmin,request,queryset):
#         for obj in queryset:
#             queryset.update(delivery_staff=i.name)
   

# def admin_actions(context):
#     context['action_index'] = context.get('action_index', -1) + 1
#     return context            



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['id','order_number','order_date','customer','schedule_shipping_date','order_type','order_amount','sales_person','delivery_guy','order_status','payment_status'] 
    list_filter=['delivery_staff','schedule_delivery_date','customer',('schedule_delivery_date',DateRangeFilter),]
    
    #actions=[allocate_staff]
    _update_fields = [(i.name,i.name,i.name) for i in StaffPerson.objects.filter(designation='delivery_guy')]

    def get_actions(self, request):
        def func_maker(value):
            def update_func(self, request, queryset):
                queryset.update(delivery_staff=value)
            return update_func

        actions = super().get_actions(request)

        for description, function_name, value in self._update_fields:
            func = func_maker(value)
            name = 'update_{}'.format(function_name)
            actions['update_{}'.format(function_name)] = (func, name, 'Assign {}'.format(description))

        return actions

   



    def order_number(self,obj):
        return obj.id

    def order_type(self,obj):
        return 'Regular'    

    def  schedule_shipping_date(self,obj):
        return obj.schedule_delivery_date 

    def delivery_guy(self,obj):
        if obj.delivery_staff == None:
            url="/admin/orders/order/{}/change/".format(obj.id)
            return mark_safe('<a href="{}">Allocate</a>'.format(url))
        else:
            return obj.delivery_staff   

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     if 'delete_selected' in actions:
    #         del actions['delete_selected']
    #     return actions    
    def has_delete_permission(self, request, obj = None):
        return False     
    def has_add_permission(self, request):
        return False           


class DeliveryMaster(Order):
    class Meta:
        proxy=True

class MyDeliveryAdmin(OrderAdmin):
    list_display=['customer','delivery_Date','order_number','product','delivery_address','quantity','delivery_staff','order_status']  

    def get_queryset(self, request):
        todaytime = datetime.now()
        todaytime = str(todaytime).split(" ")
        todaytime=todaytime[0]+" 00:00:00"
        nextday = datetime.strptime(todaytime,'%Y-%m-%d %H:%M:%S')+timedelta(days=1)
        return Order.objects.filter(schedule_delivery_date__gte=todaytime)#,schedule_delivery_date__lte=nextday) 

    def delivery_Date(self,obj):
        return obj.schedule_delivery_date    

admin.site.register(DeliveryMaster,MyDeliveryAdmin)



    