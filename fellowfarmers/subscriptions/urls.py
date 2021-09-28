from django.urls import path
from .views import *

urlpatterns = [
    path('fetchsubscriptionbycustomer/<int:custid>',fetchsubscriptionbycustomer.as_view()),
    path('fetchsubscriptionbyid/<int:subid>',fetchsubscriptionbyid.as_view()),
    path('stopsubscription/<int:subid>/<str:substatus>',stopsubscription.as_view()),
    path('testorder/',testorder),
]
