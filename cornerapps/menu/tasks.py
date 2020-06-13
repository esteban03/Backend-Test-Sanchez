from cornerapps.menu.components import ReminderMenuToday
from cornerapps.menu.factories import NotifierFactory

from celery import shared_task


@shared_task
def send_reminder_menu():
    reminder = ReminderMenuToday(notifier=NotifierFactory.create())
    reminder.send()
