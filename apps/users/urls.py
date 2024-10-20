from django.urls import path

from users.views.register import RegisterView, CustomLoginView, logout, conform_message, ConformTemplateView, \
    ForgotPasswordFormView, ForgotPasswordMessageTemplateView, ResetPasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('register-message/', ConformTemplateView.as_view(), name='register-message'),

    path('email-confirmation-message/<str:confirmation_code>/', conform_message, name='confirm-message'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordFormView.as_view(), name='forgot-password'),
    path('reset-password-message/', ForgotPasswordMessageTemplateView.as_view(), name='reset-password-message'),
    path('reset-password/<str:confirmation_code>/', ResetPasswordView.as_view(), name='reset-confirm-password'),
    path('logout/', logout, name='logout'),
]
