from slack import WebClient
from slack.errors import SlackApiError

from cornerapps.menu.interfaces import NotifierInterface
from cornerapps.menu.exceptions import NotifierError


class SlackNotifier(NotifierInterface):
    """Send message to channel Slack"""

    def __init__(self, token_api, chanel):
        self.__client = WebClient(token_api)
        self.__chanel = chanel

    def send_message(self, message):
        try:
            response = self.__client.chat_postMessage(
                channel=self.__chanel,
                text=message
            )
        except SlackApiError:
            raise NotifierError
