from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

urlpatterns = [
    path('shops/', include('shops.urls')),
    path('teligram/', include('teligram.urls')),
    path('orders/', include('orders.urls')),
    path('users/', include('users.urls')),

]
