from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from twilio.rest import Client
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
import urllib.request
import urllib.parse

# Create your views here.


def sendemailcommon(request):
    subject = request['subject']
    message = request['message']
    fromemail=settings.EMAIL_HOST_USER
    to=request['to']
    send_mail(subject, message, fromemail,to)
    return True


class sendsmsapi(APIView):

    permission_classes=[IsAuthenticated,]
    authentication_classes=[TokenAuthentication,]
    def post(self,request):
        customer_data = JSONParser().parse(request)
        print(customer_data)
        data={'body':customer_data['otp'],'to':customer_data['mobile']}
        sendsmscommon(data)
        sms={'success':True}    
        return JsonResponse(sms,safe=False)



#def sendsmscommon(request):
    # body=request['body']
    # to='+91'+request['to']
    # fromsend=settings.TWILIO_NUMBER
    # client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    # message = client.messages.create(to=to, from_=fromsend,body=body)
    # print(message.sid)
    #return True


def sendsmscommon(request):
    message="test body"#request['body']
    numbers='919870888649'#'+91'+request['to']
    sender='fellowfarmer'
    apikey=settings.TEXTLOCAL_API
    params = {'apikey': apikey, 'numbers': numbers, 'message' : message, 'sender': sender}
    f = urllib.request.urlopen('https://api.textlocal.in/send/?'
        + urllib.parse.urlencode(params))
    fr = f.read()
    print(fr)
    return True    

def testmsg(request):
    message="test body"#request['body']
    numbers='919870888649'#'+91'+request['to']
    sender='fellowfarmer'
    apikey=settings.MSG91_AUTHKEY
    flow_id='test'
    import http.client

    conn = http.client.HTTPSConnection("api.msg91.com")

    # payload = {"flow_id":"test",
    # "sender":"fellowfarmwers",
    # "mobiles": "919870888649",
    # "VAR1": "VALUE 1",
    # "VAR2":"VALUE 2"}

    payload = "{\n  \"flow_id\": \"test\",\n  \"sender\": \"fellowfarmwers\",\n  \"mobiles\": \"9870888649\",\n  \"VAR1\": \"VALUE 1\",\n  \"VAR2\": \"VALUE 2\"\n}"

    headers = {
    'authkey': "366337ATEy7MjDzn612751eeP1",
    'content-type': "application/JSON"
    }

    conn.request("POST", "/api/v5/flow/", payload, headers)

    res = conn.getresponse()
    data = res.read()
    print("nikhil")
    print(data.decode("utf-8"))
    return data.decode("utf-8")


def testlocalsms(request):
    import urllib.request
    import urllib.parse
 
    apikey="NjMzNjYxNDY1NzZmNjk0YzM5NTY3OTRkNGQ0YzZjNmY="
    numbers='9870888649'
    message="your booking is confirmed"
    sender='fellofaarmer'
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    print(fr)
    return(fr)
 

    