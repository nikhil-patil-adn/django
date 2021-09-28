"""fellowfarmers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token 
admin.site.site_header = 'FellowFarmers'

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/banners/', include('banners.urls')),
    path('api/products/',include('products.urls')),
    path('api/location/',include('societymasters.urls')),
    path('api/customers/',include('customers.urls')),
    path('api/coupons/',include('coupons.urls')),
    path('api/orders/',include('orders.urls')),
    path('api/subscriptions/',include('subscriptions.urls')),
    path('api/city/',include('othermasters.urls')),
    path('api/feedbacks/',include('feedbacks.urls')),
    path('api/frequency/',include('frequencymasters.urls')),
    path('api/myholidays/',include('myholidays.urls')),
    path('api/sendsmsemails/',include('sendsmsemails.urls')),
    path('api/staffpersons/',include('staffpersons.urls')),
    path('api/paymentlogs/',include('paymentlogs.urls')),
    #path('api-token-auth', obtain_auth_token, name='api_token_auth'), 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('commission_pay/', include('commissions.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)