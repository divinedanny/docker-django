from celery import Celery, shared_task
from django.core.mail import EmailMessage
from django.conf import settings

@shared_task(bind=True)
def send_otp(self,email, otp):
    subject = 'Verify your email'
    message = f'Your OTP is {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    mail = EmailMessage(subject, message, email_from, recipient_list)
