import uuid
from django.urls import reverse
from shared.tests import ApiTestCaseBase

from rest_framework.status import HTTP_200_OK

from cornerapps.menu.models import Menu

from faker import Faker


class TestViewMenu(ApiTestCaseBase):

    def setUp(self):
        self.faker = Faker()

    def test_success_view_menu(self):
        user, token, credentials = self.generate_chef_user()

        new_menu = {
            'id': uuid.uuid4(),
            'user': user,
            'day': self.faker.future_date(),
        }

        menu = Menu.objects.create(**new_menu)

        route = reverse('menu:view', kwargs={'id': new_menu['id']})
        response = self.client.get(route)

        self.assertTrue(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['id'], str(new_menu['id']))
        self.assertEqual(response.data['day'], str(new_menu['day']))
