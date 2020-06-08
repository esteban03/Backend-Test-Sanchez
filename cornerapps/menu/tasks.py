from app.settings import env

from django.utils import timezone
from django.urls import reverse

from celery import shared_task
from cornerapps.menu.models import Menu

from cornerapps.menu.factories import NotifierFactory


@shared_task
def send_reminder_menu():
    notifier = NotifierFactory.create()

    today = timezone.now().date()
    menu_today = Menu.objects.filter(day=today).first()

    if menu_today is None:
        return

    link_menu = "{domain}{path}".format(
        domain=env('APP_URL'),
        path=reverse('menu:view', kwargs={'id': menu_today.id})
    )

    message = "Hola! recuerden elegir el menu de hoy antes de las 11AM. Lo pueden ver aqui {}".format(link_menu)

    notifier.send_message(message=message)
