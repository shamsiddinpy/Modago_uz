from django.urls import path

from users.views.register import RegisterView, LoginView, LagoutFormView, conform_message, ConformTemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirmation-message/<str:confirmation_code>/', conform_message, name='confirm-message'),
    path('login/', LoginView.as_view(), name='login'),
    path('register-message', ConformTemplateView.as_view(), name='register-message'),
    path('logout/', LagoutFormView.as_view(), name='logout'),
]
