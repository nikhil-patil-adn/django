from django.db.models.query import QuerySet
from othermasters.models import CityMaster
from societymasters.models import SocietyMaster
from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser 
from .models import  StaffPerson
from .serializers import StaffPersonSerializer
from rest_framework.views import APIView
import random

# Create your views here.

class checkregister(APIView):
    permission_class=[IsAuthenticated]
    authentication_classes=[TokenAuthentication]
    def get(self,request,mob):
        queryset=StaffPerson.objects.filter(mobile=mob)
        cust=StaffPersonSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(cust.data,safe=False)

class checklogin(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication]
    def post(self,request):
        customer_data = JSONParser().parse(request)
        print(customer_data)
        queryset=StaffPerson.objects.filter(mobile=customer_data['mobile'],password=customer_data['password'])
        print(queryset)
        cust=StaffPersonSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(cust.data,safe=False)

class updatepassword(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]  
    def post(self,request):
        customer_data=JSONParser().parse(request)
        print(customer_data)
        StaffPerson.objects.filter(mobile=customer_data['mobile']).update(password=customer_data['password'])
        queryset=StaffPerson.objects.filter(mobile=customer_data['mobile'])
        print(queryset)
        cust=StaffPersonSerializer(queryset,context={'request':request},many=True)
        print(cust)
        return JsonResponse(cust.data,safe=False)


