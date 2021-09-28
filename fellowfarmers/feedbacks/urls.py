from django.urls import path
from .views import *

urlpatterns = [
    path('insertfeedback/',insertfeedback.as_view()),
    path('fetchfeedbackbycustomer/<str:id>',fetchfeedbackbycustomer.as_view()),
    path('test/',getfeedbackdatatest),
    path('fetchallfeedback/',fetchallfeedback.as_view()),
    path('fetchquestions/',fetchquestions.as_view()),

]
