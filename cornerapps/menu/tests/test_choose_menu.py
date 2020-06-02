from datetime import datetime

from django.urls import reverse

from rest_framework.status import HTTP_201_CREATED

from shared.tests import ApiTestCaseBase
from cornerapps.menu.models import Menu, Option

from faker import Faker


class TestChooseMenu(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('menu:store.choose')
        self.faker = Faker()

    def test_choose_menu(self):
        user, token, credentials = self.generate_employee_user()
        self.set_client_credentials(token)

        menu, options = self.create_menu(user)

        option = options.pop()

        choose = {
            'option': option.id,
            'comments': 'Sin aceite'
        }

        response = self.client.post(self.route, choose, format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertDictEqual(response.data, choose)

    def create_menu(self, user):
        today = datetime.today().date()

        options = (
            "Tallerines con helado",
            "Pure con papas fritas",
            "Carne mechada con pure",
        )

        menu = Menu.objects.create(user=user, day=today)

        new_options = []
        for option in options:
            new_options.append(
                Option.objects.create(menu=menu, description=option)
            )
        return menu, new_options
