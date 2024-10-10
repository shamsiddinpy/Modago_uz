from django.urls import path

from users.views.register import RegisterView, LoginView, LagoutFormView, confirm_register, ConformTemplateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirmation-message/<str:confirmation_code>/', confirm_register, name='confirm-register'),
    path('login/', LoginView.as_view(), name='login'),
    path('conform-message', ConformTemplateView.as_view(), name='conform-message'),
    path('logout/', LagoutFormView.as_view(), name='logout'),
]
