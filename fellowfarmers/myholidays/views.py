import datetime
from orders.serializers import OrderSerializer
from orders.models import Order
from myholidays.models import MyHoliday
from customers.models import Customer
from subscriptions.models import Subscription
from django.shortcuts import render
from django.http.response import JsonResponse,HttpResponse
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser 
from .serializers import MyHolidaySerializer
import requests

# Create your views here.


def getholidaydatatest(request):
    #url = 'http://127.0.0.1:8000/api/products/details/2'
    url='http://192.168.2.107:8000/api/myholidays/fetchholidaybycustomer/8'
    headers = {'Authorization': 'Token 8334d1d63c97cc583ac50fc034afaf5f57833251'}
    r = requests.get(url, headers=headers)
    print(r)
    return HttpResponse("hi")

class fetchholidaybycustomer(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,id):
        queryset=MyHoliday.objects.filter(customer=id).order_by('-id')
        holidays=MyHolidaySerializer(queryset,context={'request':request},many=True)
        return JsonResponse(holidays.data,safe=False)


# class updateordershedule(APIView):
#     # permission_classes=[IsAuthenticated,]
#     # authentication_classes=[TokenAuthentication,]

#     def get(self,request,id):
#         queryset=MyHoliday.objects.filter(customer=id).order_by('-id')
       
#         for i in queryset:
#             date_format = '%Y-%m-%d'
            
#             a = datetime.datetime.strptime(str(i.startdate), date_format)
#             b = datetime.datetime.strptime(str(i.enddate), date_format)
#             delta = b - a
#             daysdiff=delta.days
#             startdate = str(i.startdate).split(" ")
#             startdate = startdate[0]+" 00:00:00"
#             startdate=datetime.datetime.strptime(startdate,'%Y-%m-%d %H:%M:%S')
#             enddate = str(i.enddate).split(" ")
#             enddate = enddate[0]+" 23:23:23"
#             enddate=datetime.datetime.strptime(enddate,'%Y-%m-%d %H:%M:%S')
            
#             orderqry=Order.objects.filter(customer=id,schedule_delivery_date__gte=startdate,
#             schedule_delivery_date__lte=enddate).exclude(order_status='cancel')
#             print("noooooooooooooooooooooo")
#             if orderqry:
#                 print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")    
#                 subquery= Subscription.objects.filter(customer=id).order_by('-id')[:1]
#                 for i in subquery:
#                     new=str(i.subscription_end).split("+")
#                 orderqrylast=Order.objects.order_by('-id')[:1]
#                 for i in orderqrylast:
#                     lastid=i.id
#                 print(lastid)    
#                 print(len(orderqry))
#                 cnt=1
#                 for i in orderqry:
#                     print(i.id)
#                     if i.subscription_payment_type == 'prepaid' and i.subscription_type == 'alternate':
#                         adddays=2
#                     else:
#                         adddays=1    
#                     newshedule=datetime.datetime.strptime(str(new[0]),'%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=2)
#                     i.schedule_delivery_date=newshedule
#                     i.id=lastid+cnt
#                     cnt=cnt+1
#                     i.order_status='delivery_scheduled'
#                     i.save()
#                     new[0]=newshedule
#                     print(new[0])
#                 print(newshedule)  
#                 Subscription.objects.filter(id=subquery).update(subscription_end=newshedule)  
                
                
#             Order.objects.filter(customer=id,schedule_delivery_date__gte=startdate,
#             schedule_delivery_date__lte=enddate).update(order_status='cancel')        
 
#         holidays=MyHolidaySerializer(queryset,context={'request':request},many=True)        
#         return JsonResponse(holidays.data,safe=False)



def updateordershedule(request):
        id=request['id']
        queryset=MyHoliday.objects.filter(customer=id).order_by('-id')
       
        for i in queryset:
            date_format = '%Y-%m-%d'
            
            a = datetime.datetime.strptime(str(i.startdate), date_format)
            b = datetime.datetime.strptime(str(i.enddate), date_format)
            delta = b - a
            daysdiff=delta.days
            startdate = str(i.startdate).split(" ")
            startdate = startdate[0]+" 00:00:00"
            startdate=datetime.datetime.strptime(startdate,'%Y-%m-%d %H:%M:%S')
            enddate = str(i.enddate).split(" ")
            enddate = enddate[0]+" 23:23:23"
            enddate=datetime.datetime.strptime(enddate,'%Y-%m-%d %H:%M:%S')
            
            orderqry=Order.objects.filter(customer=id,schedule_delivery_date__gte=startdate,
            schedule_delivery_date__lte=enddate).exclude(order_status='cancel')
            print("noooooooooooooooooooooo")
            if orderqry:
                print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")    
                subquery= Subscription.objects.filter(customer=id).order_by('-id')[:1]
                for i in subquery:
                    new=str(i.subscription_end).split("+")
                orderqrylast=Order.objects.order_by('-id')[:1]
                for i in orderqrylast:
                    lastid=i.id
                print(lastid)    
                print(len(orderqry))
                cnt=1
                for i in orderqry:
                    print(i.id)
                    if i.subscription_payment_type == 'prepaid' and i.subscription_type == 'alternate':
                        adddays=2
                    else:
                        adddays=1    
                    newshedule=datetime.datetime.strptime(str(new[0]),'%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=2)
                    i.schedule_delivery_date=newshedule
                    i.id=lastid+cnt
                    cnt=cnt+1
                    i.order_status='delivery_scheduled'
                    i.save()
                    new[0]=newshedule
                    print(new[0])
                print(newshedule)  
                Subscription.objects.filter(id=subquery).update(subscription_end=newshedule)  
                
                
            Order.objects.filter(customer=id,schedule_delivery_date__gte=startdate,
            schedule_delivery_date__lte=enddate).update(order_status='cancel')        
 
              
        return True




    
class insertholiday(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def post(self,request):
        holiday_data = JSONParser().parse(request)
        print(holiday_data)
        custobj=Customer.objects.get(id=holiday_data['custid'])
        startdate = holiday_data['startdate'].split(" ")
        startdate[-1] = startdate[-1][:8]
        startdate = " ".join(startdate)
        startdate=datetime.datetime.strptime(startdate,'%Y-%m-%d %H:%M:%S')
        enddate = holiday_data['enddate'].split(" ")
        enddate[-1] = enddate[-1][:8]
        enddate = " ".join(enddate)
        enddate=datetime.datetime.strptime(enddate,'%Y-%m-%d %H:%M:%S')
        sv=MyHoliday(
            customer=custobj,
            startdate=startdate,
            enddate=enddate
        )
        sv.save()
        sheduledata={'id':holiday_data['custid']}
        updateordershedule(sheduledata)
        return JsonResponse(holiday_data,safe=False)


