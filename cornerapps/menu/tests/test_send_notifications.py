from shared.tests import ApiTestCaseBase
from cornerapps.menu.factories import NotifierFactory
from cornerapps.menu.implementations import SlackNotifier

from slack.errors import SlackApiError


class TestSendNotifications(ApiTestCaseBase):

    def test_send_success(self):
        notifier = NotifierFactory.create()
        notifier.send_message(message='test unit message')

    def test_send_fail(self):
        with self.assertRaises(SlackApiError):
            notifier = SlackNotifier(
                token_api='fail',
                chanel='fail'
            )

            notifier.send_message(message='fail')
