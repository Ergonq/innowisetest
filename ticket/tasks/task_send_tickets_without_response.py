from ticket.tasks.utils import utils as task_utils
from celery.utils.log import get_task_logger
from celery import shared_task

logger = get_task_logger(__name__)


@shared_task()
def task_to_send_tickets_without_response():
    """
    Task to send tickets without response
    """
    task_utils.send_email_to_users()
