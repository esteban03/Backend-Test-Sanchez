from app.settings import env

from django.utils import timezone
from django.urls import reverse

from cornerapps.menu.models import Menu


class ReminderMenuToday:

    def __init__(self, notifier):
        self.notifier = notifier

    def send(self):
        menu_today = Menu.objects.filter(day=timezone.now()).first()

        if menu_today is None:
            return

        link_menu = "{domain}{path}".format(
            domain=env('APP_URL'),
            path=reverse('menu:view', kwargs={'id': menu_today.id})
        )

        message = "Hola! recuerden elegir el menu de hoy antes de las 11AM. Lo pueden ver aqui {}".format(link_menu)

        self.notifier.send_message(message=message)
