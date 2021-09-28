from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from .models import Coupon
from .serializers import CouponSerializer
from rest_framework.views import APIView

# Create your views here.
class checkcoupon(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]
    def get(self,request,coupontxt):
        queryset=Coupon.objects.filter(name__iexact=coupontxt)
        cust=CouponSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(cust.data,safe=False)