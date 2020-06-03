from django.utils import timezone
from celery import shared_task
from cornerapps.menu.models import Menu

from cornerapps.menu.implementations import SlackNotifier as Notifier


@shared_task
def send_reminder_menu():
    notifier = Notifier()

    today = timezone.now().date()
    menu_today = Menu.objects.filter(day=today).first()

    if menu_today is None:
        return

    # TODO: implement route with reverse url django
    link_menu = "https://nora.cornershop.io/menu/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    message = "Hola! recuerden elegir el menu de hoy antes de las 11AM. Pueden ver el menu aqui {}".format(link_menu)

    notifier.send_message(message=message)
