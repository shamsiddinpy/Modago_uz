from django.contrib import admin
from django.contrib.messages import api
from django.urls import path, include

from users.views.register import RegisterView, LoginView, LagoutFormView, confirm_register

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirmation-message/<str:confirmation_code>/', confirm_register, name='confirm-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LagoutFormView.as_view(), name='logout'),
]
