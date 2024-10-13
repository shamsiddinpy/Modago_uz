from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(request, email: str, confirmation_code: str):
    link = request.build_absolute_uri(f'/users/email-confirmation-message/{confirmation_code}/')

    context = {
        'link': link
    }

    html_message = render_to_string('apps/auth/email_message.html', context)
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject='Salom, xush kelibsiz BotCommerce',
        body=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    message.attach_alternative(html_message, 'text/html')
    message.send()


def send_password_reset_email(request, email: str, confirmation_code: str):
    link = request.build_absolute_uri(f'/users/reset-password/{confirmation_code}')

    context = {
        'link': link
    }

    html_message = render_to_string('apps/auth/resed_email_message.html', context)
    plain_message = strip_tags(html_message)

    message = EmailMultiAlternatives(
        subject="Parolni tiklash - Modago",
        body=plain_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )
    message.attach_alternative(html_message, 'text/html')
    message.send()

    # http://localhost:8000/api/v1/user/sign-up/email-confirmation-message/PpOiFKWrRNmGfjEdrVYJ57QQ7jALQ8e1
