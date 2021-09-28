from django.urls import path
from .views import *

urlpatterns = [
    path('insertholidays/',insertholiday.as_view()),
    path('test',getholidaydatatest),
    path('fetchholidaybycustomer/<int:id>',fetchholidaybycustomer.as_view()),
    #path('updateordershedule/<int:id>',updateordershedule.as_view()),

]
