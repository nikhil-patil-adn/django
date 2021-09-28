from orders.models import Order
from django.db.models.query import QuerySet
from django.http.response import JsonResponse,HttpResponse
import datetime

from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser 
from products.models import Product
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework.views import APIView
import requests

# Create your views here.

def testorder(request):
    #url='http://192.168.2.107:8000/api/order/getordersbycust/8'
    url='http://127.0.0.1:8000/api/subscriptions/fetchsubscriptionbycustomer/8'
    headers = {'Authorization': 'Token 8334d1d63c97cc583ac50fc034afaf5f57833251'}
    r = requests.get(url, headers=headers)
    print(r)
    return HttpResponse("hi")


class fetchsubscriptionbyid(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,subid):
        QuerySet=Subscription.objects.filter(id=subid)
        orderdata=SubscriptionSerializer(QuerySet,context={'request':request},many=True)
        return JsonResponse(orderdata.data,safe=False)

class stopsubscription(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,subid,substatus):
        subdata=Subscription.objects.filter(id=subid).values('subscription_end','customer')
        if substatus == 'resume':
            substatus='active'
        

        Subscription.objects.filter(id=subid).update(status=substatus)
        todaydate=datetime.datetime.today().strftime('%Y-%m-%d')
        todaydate="{} 00:00:00".format(todaydate)
        enddate=str(subdata[0]['subscription_end']).split('+')
        enddate=enddate[0]
        if substatus == 'active':
            orderstatus='delivery_scheduled'
        else:
            orderstatus='cancel'    

        orderdata=Order.objects.filter(schedule_delivery_date__gte=todaydate,
        schedule_delivery_date__lte=enddate,
        customer=subdata[0]['customer']).update(order_status=orderstatus)
        QuerySet=Subscription.objects.filter(id=subid)
        subdata=SubscriptionSerializer(QuerySet,context={'request':request},many=True)
        
        return JsonResponse(subdata.data,safe=False)

class fetchsubscriptionbycustomer(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,custid):
        QuerySet=Subscription.objects.filter(customer=custid)
        orderdata=SubscriptionSerializer(QuerySet,context={'request':request},many=True)
        return JsonResponse(orderdata.data,safe=False)
