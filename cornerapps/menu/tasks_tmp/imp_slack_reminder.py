from slack import WebClient
from slack.errors import SlackApiError

from cornerapps.menu.models import Menu
from django.utils import timezone


def send_message():
    slack_token = "xoxb-1184690602240-1160854967714-zRHjFJiGVjREfnvBoMCSs0pT"
    client = WebClient(token=slack_token)

    try:
        today = timezone.now().date()
        menu = Menu.objects.filter(day=today).first()

        if Menu is None:
            return

        link_menu = "https://nora.cornershop.io/menu/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
        message = "Hola! recuerden elegir el menu de hoy antes de las 11AM. Pueden ver el menu aqui {}".format(link_menu)

        response = client.chat_postMessage(
            channel="cornerapp",
            text=message
        )
    except SlackApiError as e:
        assert e.response["error"]

