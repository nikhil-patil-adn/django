from django.http.response import JsonResponse
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from .models import CityMaster
from .serializers import CitySerializer
from rest_framework.views import APIView


# Create your views here.



class getcitybyid(APIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,cityid):
        print(cityid)
        queryset=CityMaster.objects.filter(id__iexact=cityid)
        print(queryset)
        soc=CitySerializer(queryset,context={'request':request},many=True)
        return JsonResponse(soc.data,safe=False)


class allCity(APIView):

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        queryset=CityMaster.objects.all()
        soc=CitySerializer(queryset,context={'request':request},many=True)
        return JsonResponse(soc.data,safe=False)           