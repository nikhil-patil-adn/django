from django.urls import path
from .views import *

urlpatterns = [
    path('fetchfrquencyall/',fetchfrquencyall.as_view()),
    path('fetchfrquencybyproduct/<str:id>',fetchfrquencybyproduct.as_view()),
    path('test/',test),
]
