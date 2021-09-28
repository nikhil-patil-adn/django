from django.urls import path
from .views import *

urlpatterns = [
    path('getcitybyid/<str:cityid>',getcitybyid.as_view()),
    path('allcity/',allCity.as_view()),
    
]
