from celery import shared_task
from cornerapps.menu.tasks_tmp.imp_slack_reminder import send_message

@shared_task
def send_slack_message():
    send_message()