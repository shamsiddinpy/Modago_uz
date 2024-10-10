from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

from shops.views.dashboard import DashboardView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
