from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from .models import Paymentlog
from .serializers import PaymentlogSerializer


# Create your views here.


class fetchlogsbycustomer(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def get(self,request,custid):
        QuerySet=Paymentlog.objects.filter(customerid=custid)
        orderdata=PaymentlogSerializer(QuerySet,context={'request':request},many=True)   
        return JsonResponse(orderdata.data,safe=False)
