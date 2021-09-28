from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .models import Product
from .views import *

router=DefaultRouter()
router.register(r'fetch_products',fetchProduct)
#router.register(r'details/(?P<code>\d+)',fetchProductDetail,basename='Product')


urlpatterns = [
    path('', include(router.urls)),
    path('details/<int:code>',fetchProductDetail.as_view()),
    #path('details/<int:code>',fetchProductDetail),
    path('getproductdatatest',getproductdatatest),
]