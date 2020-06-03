from app.settings import env

from slack import WebClient
from slack.errors import SlackApiError

from cornerapps.menu.interfaces import NotifierInterface


class SlackNotifier(NotifierInterface):
    """Send message to channel Slack"""

    def __init__(self):
        self.__client = WebClient(token=env("SLACK_TOKEN_API"))
        self.__chanel = env("SLACK_CHANNEL_SEND_MESSAGE")

    def send_message(self, message):
        try:
            response = self.__client.chat_postMessage(
                channel=self.__chanel,
                text=message
            )
        except SlackApiError as e:
            assert e.response["error"]
