from django.urls import path
from .views import *

urlpatterns = [
    path('insertorder/',insertorder.as_view()),
    path('getordersbycust/<int:custid>',getordersbycust.as_view()),
    path('fetchbuynowbycustomer/<int:custid>',fetchbuynowbycustomer.as_view()),
    path('deliveryguyorders/<int:custid>',deliveryguyorders.as_view()),
    path('updatestatus/<int:orderid>/<str:status>',updatestatus.as_view()),
    path('get_staff/',get_staff),

    path('test/',testorder),
]
