from django.urls import path

from users.views.register import RegisterView, LoginView, LogoutFormView, conform_message, ConformTemplateView, \
    ForgotPasswordFormView, ForgotPasswordMessageTemplateView, ResetPasswordTemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register-message', ConformTemplateView.as_view(), name='register-message'),

    path('email-confirmation-message/<str:confirmation_code>/', conform_message, name='confirm-message'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordFormView.as_view(), name='forgot-password'),
    path('reset-password-message/', ForgotPasswordMessageTemplateView.as_view(), name='forgot-password-message'),
    path('reset-password/<str:confirmation_code>/', ResetPasswordTemplateView.as_view(), name='reset-password'),
    path('logout/', LogoutFormView.as_view(), name='logout'),
]
