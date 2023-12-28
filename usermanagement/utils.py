from django.core.mail import send_mail
from django.template.loader import get_template


def send_reset_password_email(email, redirect_url):
    data = {
        'redirect_url': redirect_url
    }
    message = f"{get_template('reset_password_email.html').render(data)}"
    send_mail(
        subject='Please Reset Password',
        message=message,
        from_email='admin@admin.com',
        recipient_list=[email],
        fail_silently=False,
    )
