from django.urls import path
from .views import *

urlpatterns = [
    path('getsociety/<str:soc>',getAllSociety.as_view()),
    path('getsocietybyid/<str:socid>',getsocietybyid.as_view()),
    path('allsociety/',allSociety.as_view()),
    
]
