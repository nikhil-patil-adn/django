from django.urls import path
from .views import *


urlpatterns = [
    path('checklogin/',checklogin.as_view()),
    path('checkregister/<str:mob>',checkregister.as_view()),
    path('updatepasswordstaff/',updatepassword.as_view()),
]
