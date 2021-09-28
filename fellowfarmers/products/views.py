from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import viewsets
from .models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
import requests

# Create your views here.
class fetchProduct(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


# class fetchProductDetail(viewsets.ModelViewSet):

#     serializer_class=ProductSerializer

#     def get_queryset(self):
#         print(self.kwargs)
#         queryset=Product.objects.filter(code=self.kwargs['code'])
#         return queryset


# def fetchProductDetail(request,code):
#     queryset=Product.objects.filter(code=code)
#     products=ProductSerializer(queryset,context={'request':request},many=True)
#     return JsonResponse(products.data,safe=False)



def getproductdatatest(request):
    #url = 'http://127.0.0.1:8000/api/products/details/2'
    url='http://192.168.2.101:8000/api/location/getsociety'
    headers = {'Authorization': 'Token 8334d1d63c97cc583ac50fc034afaf5f57833251'}
    r = requests.get(url, headers=headers)
    return HttpResponse("hi")
    
    

class fetchProductDetail(APIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,code):
        queryset=Product.objects.filter(code=code)
        products=ProductSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(products.data,safe=False)