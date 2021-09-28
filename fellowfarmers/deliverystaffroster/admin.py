from django.contrib import admin
from django.contrib.admin.filters import SimpleListFilter
from rangefilter.filters import DateRangeFilter
from .models import DeliveryStaffRoster
from django.utils.safestring import mark_safe 
from datetime import timedelta,datetime
# Register your models here.

class staff_name(SimpleListFilter):
    title = 'Staff Name'
    parameter_name = 'staff'

    def lookups(self, request, model_admin):
        staffname = set([c.staff for c in model_admin.model.objects.all()])
        return [(c.id, c.name) for c in staffname]

    def queryset(self, request, queryset):
        if self.value() == None:
            return queryset.all()
        else:    
            return queryset.filter(staff__id__exact=self.value())      




@admin.register(DeliveryStaffRoster)
class DeliveryStaffRosterAdmin(admin.ModelAdmin):
    list_display=['date_of_attendance','attendace_status','staff_name','todays_deliveries_assign']
    list_filter=[staff_name,('date_of_attendance',DateRangeFilter)]
    date_hierarchy ='date_of_attendance'

    def has_delete_permission(self, request, obj = None):
        return False  

    # def get_queryset(self, request):
    #     todaytime = datetime.now()
    #     end_date = datetime.datetime(todaytime.year, todaytime.month, todaytime.day)
    #     nextday = datetime.now()
    #     nextday += timedelta(days=1)
    #     return DeliveryStaffRoster.objects.all() 

    def staff_name(self,obj):
        return obj.staff.name

    def todays_deliveries_assign(self,obj):
        todaytime = datetime.now()
        nextday = datetime.now()
        nextday += timedelta(days=1)
        url="/admin/orders/order/?delivery_staff__exact={}&schedule_delivery_date__gte={}".format(obj.staff.name,todaytime)
        return mark_safe('<a href="{}">Check Deliveries</a>'.format(url))
        
#delivery_staff__exact=raj&schedule_delivery_date__gte=2021-07-20+00%3A00%3A00%2B00%3A00&schedule_delivery_date__lt=2020-02-21+00%3A00%3A00%2B00%3A00
        
#delivery_staff__exact=raj&schedule_delivery_date__gte=2021-07-20+00%3A00%3A00%2B00%3A00&schedule_delivery_date__lt=2021-07-21+00%3A00%3A00%2B00%3A00

    def get_rangefilter_date_of_attendance_default(self, request):
        return (datetime.now, datetime.now)    
               




    