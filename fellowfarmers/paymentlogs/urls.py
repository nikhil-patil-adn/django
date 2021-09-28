from django.urls import path
from .views import *

urlpatterns = [
   path('fetchlogsbycustomer/<int:custid>',fetchlogsbycustomer.as_view()),

]
