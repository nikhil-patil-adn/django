from django.urls import path
from .views import *

urlpatterns = [
    path('checkcoupon/<str:coupontxt>',checkcoupon.as_view()),
    
]
