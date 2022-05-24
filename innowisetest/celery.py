import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "innowisetest.settings")

app = Celery("innowisetest")
app.config_from_object("django.conf:settings")

app.conf.beat_schedule = {
    "send-email-once-a-week": {
        "task": "ticket.tasks.task_send_tickets_without_response.task_to_send_tickets_without_response",
        "schedule": crontab(hour=12, minute=0, day_of_week=1),
    }
}


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
