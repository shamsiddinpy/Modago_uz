from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import TemplateView, CreateView, FormView

from shared.utls.email_message import send_email
from users.forms import RegistrationUserCreationForm, LoginUserAuthenticationForm
from users.models import User


class RegisterView(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = RegistrationUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = User.Type.EMAIL
        user.save()
        confirmation_code = get_random_string(32)
        user.confirmation_code = confirmation_code
        user.save()
        send_email(self.request, user.email, confirmation_code)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def confirm_register(request, confirmation_code):
    user = get_object_or_404(User, confirmation_code=confirmation_code)
    if user.is_active:
        return HttpResponse('Email allaqachon tasdiqlangan.')

    user.is_active = True
    user.public_offer = True
    user.confirmation_code = ''
    user.save()
    login(request, user)
    return redirect('login')


class LoginView(FormView):
    template_name = 'apps/auth/login.html'
    form_class = LoginUserAuthenticationForm
    success_url = reverse_lazy('logout')

    def form_invalid(self, form):
        return super().form_invalid(form)


class LagoutFormView(TemplateView):
    template_name = 'apps/auth/test.html'
    # form_class = LoginUserAuthenticationForm
