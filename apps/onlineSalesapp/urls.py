from django.urls import path
from rest_framework import routers
from apps.onlineSalesapp.views import *


router = routers.DefaultRouter()

router.register(r"api/onlineSale", OnlineSale,  basename='online-sale')

urlpatterns = [
    
]

urlpatterns += router.urls