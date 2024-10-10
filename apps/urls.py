from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

urlpatterns = [
    path('shops/', include('shops.urls')),
    path('telegram/', include('telegram.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),

]
