from django.urls import reverse

from rest_framework.status import HTTP_200_OK

from shared.tests import ApiTestCaseBase
from cornerapps.menu.serializers import StoreMenuSerializer

from faker import Faker


class TestUpdateMenu(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('menu:update')
        self.faker = Faker()

    def test_update_menu_success(self):
        day_after_today = self.faker.date_this_month(before_today=False, after_today=True)

        serializer = StoreMenuSerializer(data={
            'day': day_after_today,
            'options': [
                "Tallerines con helado",
                "Pure con papas fritas",
                "Carne mechada con pure",
            ]
        })

        serializer.is_valid()
        menu = serializer.save()

        menu_options = menu.options.all()

        user, token, credentials = self.generate_chef_user()
        self.set_client_credentials(token)

        day_after_today_update = self.faker.date_this_month(before_today=False, after_today=True)

        update_menu = {'day': day_after_today_update, 'options': []}

        for option in menu_options:
            update_menu['options'].append({
                'id': option.pk,
                'description': 'update food',
            })

        response = self.client.post(self.route, update_menu)

        self.assertEqual(response.status_code, HTTP_200_OK)
