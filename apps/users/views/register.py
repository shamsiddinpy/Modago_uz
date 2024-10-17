from django.contrib.auth import login
from django.core.cache import cache
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.views.generic import TemplateView, CreateView, FormView

from shared.utls.email_message import send_email, send_password_reset_email
from shops.models import Shop
from users.forms import RegistrationUserCreationForm, LoginUserAuthenticationForm, ForgotPasswordForm, ResetPasswordForm
from users.models import User


class RegisterView(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = RegistrationUserCreationForm
    success_url = reverse_lazy('register-message')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.type = User.Type.EMAIL
        user.save()
        confirmation_code = get_random_string(32)
        cache.set(confirmation_code, user.email, 3600)
        user.confirmation_code = confirmation_code
        user.save()
        send_email(self.request, user.email, confirmation_code)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


def conform_message(request, confirmation_code):
    email = cache.get(confirmation_code)

    user = get_object_or_404(User, email=email)
    user.is_active = True
    user.public_offer = True
    user.confirmation_code = ''
    user.save()
    login(request, user)
    return redirect('login')


class LoginView(FormView):
    template_name = 'apps/auth/login.html'
    form_class = LoginUserAuthenticationForm
    success_url = reverse_lazy('select_shop')

    def form_invalid(self, form):
        user = form.get_user()
        login(self.request, user)
        if Shop.objects.filter(owner=user).exists():
            shop = Shop.objects.filter(owner=user).first()
            return redirect('shop', pk=shop.pk)

        else:
            return redirect('select_shop')
        return super().form_invalid(form)


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')


class ConformTemplateView(TemplateView):
    template_name = 'apps/auth/register-message.html'


class ForgotPasswordFormView(FormView):
    template_name = 'apps/auth/forgot-password.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('reset-password-message')

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        user = get_object_or_404(User, email=email)
        conform_code = get_random_string(32)
        cache.set(conform_code, user.email, 3600)
        user.confirmation_code = conform_code
        user.save()
        send_password_reset_email(self.request, user.email, conform_code)
        return super().form_valid(form)


class ResetPasswordView(FormView):
    template_name = 'apps/auth/reset-password.html'
    form_class = ResetPasswordForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['confirmation_code'] = self.kwargs.get('confirmation_code')  # URL'dan confirmation_code ni olish
        return context

    def form_valid(self, form):
        confirmation_code = self.kwargs.get('confirmation_code')
        email = cache.get(confirmation_code)
        if not email:
            form.add_error(None, "Tasdiqlash kodi noto'g'ri yoki muddati tugagan")
            return self.form_invalid(form)
        user = get_object_or_404(User, email=email)
        new_password = form.cleaned_data.get('new_password')
        user.set_password(new_password)
        user.confirmation_code = None
        user.save()
        cache.delete(confirmation_code)
        return redirect('login')


class ForgotPasswordMessageTemplateView(TemplateView):
    template_name = 'apps/auth/forgot-message.html'
