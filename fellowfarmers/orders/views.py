from othermasters.models import CityMaster
from paymentlogs.models import Paymentlog
from customers.serializers import CustomerSerializer
from staffpersons.models import StaffPerson
from django.db.models.query import QuerySet
from django.http.response import JsonResponse,HttpResponse
import datetime
from sendsmsemails.views import sendemailcommon,sendsmscommon
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser 
from customers.models import Customer
from products.models import Product
from subscriptions.models import Subscription
from .models import Order
from .serializers import OrderSerializer
from rest_framework.views import APIView
import json
import requests

# Create your views here.

def testorder(request):
    #url='http://192.168.2.107:8000/api/order/getordersbycust/8'
    url='http://127.0.0.1:8000/api/orders/fetchsubscriptiobycustomer/8'
    headers = {'Authorization': 'Token 8334d1d63c97cc583ac50fc034afaf5f57833251'}
    r = requests.get(url, headers=headers)
    print(r)
    return HttpResponse("hi")

class fetchbuynowbycustomer(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,custid):
        QuerySet=Order.objects.filter(customer=custid,order_type='buynow').order_by('-id')
        orderdata=OrderSerializer(QuerySet,context={'request':request},many=True)
        return JsonResponse(orderdata.data,safe=False)  

class deliveryguyorders(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,custid):
        staffobj=StaffPerson.objects.get(id=custid)
        QuerySet=Order.objects.filter(delivery_staff=staffobj)
        orderdata=OrderSerializer(QuerySet,context={'request':request},many=True)
        return JsonResponse(orderdata.data,safe=False)            

class getordersbycust(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,custid):
        QuerySet=Order.objects.filter(customer=custid).exclude(order_status='cancel')
        orderdata=OrderSerializer(QuerySet,context={'request':request},many=True)   
        return JsonResponse(orderdata.data,safe=False)


class updatestatus(APIView):

    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]
    def get(self,request,orderid,status):
        Order.objects.filter(id=orderid).update(order_status=status)
        queryset=Order.objects.filter(id=orderid)
        orderdata=OrderSerializer(queryset,context={'request':request},many=True)
        custquery=Customer.objects.filter(id=orderdata.data[0]['customer']['id'])
        cust=CustomerSerializer(custquery,many=True)
        smsdata={'body':'your order status is '+status.replace('_', ' ').lower(),'to':cust.data[0]['mobile']}
        sendsmscommon(smsdata)
        return JsonResponse(orderdata.data,safe=False)



def get_staff(request):
    phases = {}
    prophases = StaffPerson.objects.all().phase
    phases = {pp.phase.name:pp.pk for pp in prophases}
    return JsonResponse(data=phases, safe=False)





class insertorder(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]
    def post(self,request):
        customer_data = JSONParser().parse(request)
        cust=Customer.objects.get(mobile=customer_data['mobile'])
        prd=Product.objects.get(id=customer_data['selectedproductcode'])
        cityobj=CityMaster.objects.get(name=customer_data['city'])
        salespersonid=StaffPerson.objects.filter(city=cityobj,designation='sales_person').values('pk')
        salesperson=StaffPerson.objects.get(id=salespersonid[0]['pk'])
        deliveryaddress=customer_data['address']+","+customer_data['society']+","+customer_data['city']+","+customer_data['pincode']
        if customer_data['btntype'] == 'subscription':
            diffday=1 

            # if customer_data['prepaidoption'] == '1':
            #     daysrange=31
            # elif customer_data['prepaidoption'] == '2':
            #     daysrange=61
            # elif customer_data['prepaidoption'] == '3':
            #     daysrange=91 
            if customer_data['prepaidoption'] > '1':
                daysrange=int(customer_data['prepaidoption'])+int(1)  
            elif customer_data['subscriptionpaymenttype'] == 'postpaid':
                daysrange=16  
                
            if customer_data['subscriptiontype'] == 'alternate':
                diffday=2          
            selecteddate=customer_data['selecteddate']
            selecteddate = selecteddate.split(" ")
            selecteddate[-1] = selecteddate[-1][:8]
            selecteddate = " ".join(selecteddate)
            enddate=datetime.datetime.strptime(selecteddate,'%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=30)
            ss=Subscription(
                subscription_start=customer_data['selecteddate'],
                subscription_end=enddate,
                customer=cust,
                delivery_address=deliveryaddress,
                product=prd,
                status='active',
                quantity=customer_data['quantity'],
                price=customer_data['prize'],
                subscription_type=customer_data['subscriptionpaymenttype'],
                frequency_type=customer_data['subscriptiontype']
            )
            ss.save()
            subid=Subscription.objects.latest('id')
            pp=Paymentlog(
                order_type=customer_data['btntype'],
                order_id=subid,
                price=customer_data['prize'],
                transaction_id=customer_data['transactionid'],
                customerid=cust
            )
            pp.save()
            for x in range(1,daysrange,diffday):
                shipday=x-1
                newshipdate=datetime.datetime.strptime(selecteddate,'%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=shipday)

                sv=Order(
                customer=cust,
                delivery_address=deliveryaddress,
                product=prd,
                quantity=customer_data['quantity'],
                order_type=customer_data['btntype'],
                order_amount=customer_data['prize'],
                order_status='delivery_scheduled',
                payment_status='paid',
                sales_person=salesperson,
                subscription_type=customer_data['subscriptiontype'],
                subscription_payment_type=customer_data['subscriptionpaymenttype'],
                prepaid_option=customer_data['prepaidoption'],
                schedule_delivery_date=newshipdate)
                sv.save()
            orderdata = Order.objects.values().latest('id')
            msg="Congratulation your order is confirm."\
                +"product name : {}".format(prd)\
                +"quantity : {}".format(customer_data['quantity'])
            subject="Order Placed"    
            data={'message':msg,'subject':subject,
            'to':[customer_data['email']]}
            sendemailcommon(data) 
            data={'body':'test nikhil','to':customer_data['mobile']}
            sendsmscommon(data)
            return JsonResponse(orderdata,safe=False)
        else:
            selecteddate=customer_data['selecteddate']
            selecteddate = selecteddate.split(" ")
            selecteddate[-1] = selecteddate[-1][:8]
            selecteddate = " ".join(selecteddate)
            enddate=datetime.datetime.strptime(selecteddate,'%Y-%m-%d %H:%M:%S')+datetime.timedelta(days=1)
            sv=Order(
            customer=Customer.objects.get(mobile=customer_data['mobile']),
            delivery_address=customer_data['address']+","+customer_data['society']+","+customer_data['city']+","+customer_data['pincode'],
            product=Product.objects.get(id=customer_data['selectedproductcode']),
            quantity=customer_data['quantity'],
            order_type=customer_data['btntype'],
            order_amount=customer_data['prize'],
            order_status='delivery_scheduled',
            payment_status='paid',
            sales_person=salesperson,
            subscription_type=customer_data['subscriptiontype'],
            subscription_payment_type=customer_data['subscriptionpaymenttype'],
            prepaid_option=customer_data['prepaidoption'],
            schedule_delivery_date=enddate)
           
            sv.save()
            orderdata = Order.objects.values().latest('id')
            print(orderdata)
            subid=Order.objects.latest('id')
            pp=Paymentlog(
                order_type=customer_data['btntype'],
                order_id=subid,
                price=customer_data['prize'],
                transaction_id=customer_data['transactionid'],
                customerid=cust
            )
            pp.save()
            msg="Congratulation your order is confirm."\
                +"product name : {}".format(prd)\
                +"quantity : {}".format(customer_data['quantity'])
            subject="Order Placed"    
            data={'message':msg,'subject':subject,
            'to':[customer_data['email']]}
            sendemailcommon(data) 
            data={'body':'order confirmed','to':customer_data['mobile']}
            sendsmscommon(data)
            return JsonResponse(orderdata,safe=False)






        
        
        
