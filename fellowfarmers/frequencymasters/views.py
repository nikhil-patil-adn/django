from django.http.response import JsonResponse,HttpResponse
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.parsers import JSONParser 
from .models import FrequencyMaster
from .serializers import FrequencyMasterSerializer
from rest_framework.views import APIView
import requests

# Create your views here.


def test(request):
    url='http://192.168.2.107:8000/api/frequency/fetchfrquencyall/'
    headers = {'Authorization': 'Token 8334d1d63c97cc583ac50fc034afaf5f57833251'}
    r = requests.get(url, headers=headers)
    print(r)
    return HttpResponse("hi")


class fetchfrquencyall(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,] 

    def get(self,request):
        queryset=FrequencyMaster.objects.all()    
        fdata=FrequencyMasterSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(fdata.data,safe=False)


class fetchfrquencybyproduct(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,] 

    def get(self,request,id):
        queryset=FrequencyMaster.objects.filter(product__in=id,is_active=True)    
        fdata=FrequencyMasterSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(fdata.data,safe=False)        
