from celery import shared_task
from django.core.mail import send_mail

@shared_task
def bar():
  return "Hello world"
@shared_task
def send_daily_email(user_email):
    send_mail(
        subject="Напоминание о новинках",
        message="Здравствуйте! Напоминаем вам о новинках в нашем онлайн-кинотеатре!.",
        from_email='email@example.com',
        recipient_list=[user_email],
    )