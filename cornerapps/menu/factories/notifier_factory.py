from app.settings import env
from cornerapps.menu.implementations import SlackNotifier


class NotifierFactory:

    @staticmethod
    def create():
        return SlackNotifier(
            token_api=env("SLACK_TOKEN_API"),
            chanel=env("SLACK_CHANNEL_SEND_MESSAGE")
        )
