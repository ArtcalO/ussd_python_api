from django.urls import path, include
from .views import *
#from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('', uss_callback, name="ussd"),
    #path('/transfert', transfert_callback, name="ussd"),
]
