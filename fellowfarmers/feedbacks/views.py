from django.http.response import JsonResponse,HttpResponse
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import JSONParser 
from customers.models import Customer
from .models import Feedback, FeedbackQuestion
from .serializers import FeedbackSerializer,FeedbackQuestionSerializer
from rest_framework.views import APIView
import json
import requests

# Create your views here.

def getfeedbackdatatest(request):
    #url = 'http://127.0.0.1:8000/api/products/details/2'
    url='http://192.168.2.101:8000/api/feedbacks/fetchallfeedback/'
    headers = {'Authorization': 'Token 8334d1d63c97cc583ac50fc034afaf5f57833251'}
    r = requests.get(url, headers=headers)
    print(r)
    return HttpResponse("hi")


class insertfeedback(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]

    def post(self,request):
        feedback_data = JSONParser().parse(request)
        print(feedback_data)
        cust=Customer.objects.get(mobile__iexact=feedback_data['mobile'])
        sv=Feedback(customer=cust,type=feedback_data['type'],
        details=feedback_data['comment'],
        status='open')
        sv.save()
        return JsonResponse(feedback_data,safe=False)


class fetchfeedbackbycustomer(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,] 

    def get(self,request,id):
        queryset=Feedback.objects.filter(customer=id)    
        feedbackdata=FeedbackSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(feedbackdata.data,safe=False)


class fetchallfeedback(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,] 

    def get(self,request):
        queryset=Feedback.objects.all()    
        feedbackdata=FeedbackSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(feedbackdata.data,safe=False)


class fetchquestions(APIView):
    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,] 

    def get(self,request):
        queryset=FeedbackQuestion.objects.all()    
        feedbackdata=FeedbackQuestionSerializer(queryset,context={'request':request},many=True)
        return JsonResponse(feedbackdata.data,safe=False)        

