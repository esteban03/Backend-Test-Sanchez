from unittest import mock

from django.utils import timezone

from shared.tests import ApiTestCaseBase
from cornerapps.menu.interfaces import NotifierInterface
from cornerapps.menu.exceptions import NotifierError

from cornerapps.menu.components import ReminderMenuToday
from cornerapps.menu.models import Menu


class TestSendNotifications(ApiTestCaseBase):

    def setUp(self):
        new_user, token, credentials = self.generate_chef_user()
        Menu.objects.create(user=new_user, day=timezone.now())
        self.notifier_mock = mock.create_autospec(NotifierInterface)

    def test_send_success(self):
        reminder = ReminderMenuToday(notifier=self.notifier_mock)
        reminder.send()

        self.assertEqual(self.notifier_mock.send_message.call_count, 1)

    def test_send_fail(self):
        with self.assertRaises(NotifierError):
            self.notifier_mock.send_message.side_effect = NotifierError

            reminder = ReminderMenuToday(notifier=self.notifier_mock)
            reminder.send()

            self.assertEqual(self.notifier_mock.send_message.call_count, 1)
