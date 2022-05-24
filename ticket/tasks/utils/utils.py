from django.core.mail import send_mail
from ticket.models import Ticket
import environ


def get_tickets_without_admin_response():
    return Ticket.objects.filter(admin_response="").count()


def send_email_to_users():
    env = environ.Env()
    env.read_env()
    number_of_tickets_without_admin_response = get_tickets_without_admin_response()
    admin_email = env("EMAIL_HOST")
    to_email = env("EMAIL_HOST")
    send_mail(
        "Admin Notification",
        f"There are {number_of_tickets_without_admin_response} tickets without admin response!",
        admin_email,
        [to_email],
        fail_silently=False,
    )
