from django.contrib import admin
from django.contrib.admin.decorators import register
from django.utils.safestring import mark_safe  
from django.contrib.auth.models import Group,User
from admin_interface.models import Theme
from .models import Customer, Favourite
# Register your models here.

#admin.site.unregister(Group)
#admin.site.unregister(User)
admin.site.unregister(Theme)

def apply_active(modeladmin, request, queryset):
    for obj in queryset:
        if obj.active == True:
            newactive=False
        else:
            newactive=True    
        Customer.objects.filter(pk=obj.id).update(active=newactive)

apply_active.short_description = 'Active/Deactive'

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=['name','username','password','mobile','society','city','active','action']
    actions=[apply_active,]

    def action(self,obj):
        print(obj)
        viewsuburl="/admin/subscriptions/subscription/?id={}".format(obj.id)
        vieworderurl="/admin/orders/order/?id={}".format(obj.id)
        editurl="/admin/customers/customer/{}/change/".format(obj.id)
        return mark_safe('<a href="{}">view Subscription | </a> <a href="{}">view order | </a> <a class="changelink" href="{}"></a>'.format(viewsuburl,vieworderurl,editurl))
        
    def has_delete_permission(self, request, obj = None):
        return False  

    def view_subscription(self,obj):
        url="/admin/subscriptions/subscription/?id={}".format(obj.id)
        return mark_safe('<a href="{}">view subscription</a>'.format(url))

    def view_orders(self,obj):
        url="/admin/orders/order/?id={}".format(obj.id)
        return mark_safe('<a href="{}">view orders</a>'.format(url))

    def active_deactive(self,obj):
        print(obj.id)
        cust=Customer.objects.get(id=obj.id)
        print(cust)
        print(cust.active)
        if cust.active == True:
            cust.active=False
            cust.save()
            img='<img alt="True" src="/static/admin/img/icon-no.svg">'
        else:
            cust.active=True
            cust.save()
            img='<img alt="True" src="/static/admin/img/icon-yes.svg">'
        print(cust.active)
        print(img)

        return  mark_safe('{}'.format(img))  


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display=['customer','product',]   
    
    def has_delete_permission(self, request, obj = None):
        return False       

       
