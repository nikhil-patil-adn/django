from django.urls import path
from .views import *


urlpatterns = [
    path('checkregister/<str:mob>',checkregister.as_view()),
    path('customerregister/',customerregister.as_view()),
    path('checklogin/',checklogin.as_view()),
    path('customerregisterwithuserpass/',customerregisterwithuserpass.as_view()),
    path('updatepassword/',updatepassword.as_view()),
    path('checkmobile/<str:mob>',checkmobile.as_view()),
    path('addfavourite/',addfavourite.as_view()),
]
