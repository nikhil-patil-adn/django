from django.urls import path
from .views import *

urlpatterns = [
    path('sendsmsapi/',sendsmsapi.as_view()),
    path('testsms/',testlocalsms),
   
]
