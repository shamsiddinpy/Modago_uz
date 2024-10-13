from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

from shops.views.dashboard import DashboardView
from shops.views.select_shop import SelectShopTemplateView

urlpatterns = [
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('select-shop', SelectShopTemplateView.as_view(), name='select_shop'),
]
