from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import EmailField, Form, CharField, PasswordInput

from users.models import User


class RegistrationUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']


class LoginUserAuthenticationForm(Form):
    email = EmailField(max_length=254)
    password1 = CharField(strip=False, widget=PasswordInput)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(LoginUserAuthenticationForm, self).__init__(*args, **kwargs)

    def clean(self):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        if email and password1:
            self.user_cache = authenticate(self.request, email=email, password1=password1)
            if self.user_cache is None:
                raise ValidationError("Elektron pochta yoki parol noto'g'ri")
            else:
                if not self.user_cache.is_active:
                    raise ValidationError("Bu foydalanuvchi hisobi faol emas.")
        return self.cleaned_data

    def get_user(self):
        return self.user_cache
