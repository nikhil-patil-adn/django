from django.urls import path
from .views import *

urlpatterns = [
    path('payment/<int:id>',commissionpay_view, name='commission-pay'),
    ]   