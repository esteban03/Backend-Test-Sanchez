from django.urls import reverse
from shared.tests import ApiTestCaseBase

from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN, HTTP_400_BAD_REQUEST

from cornerapps.menu.models import Menu

from faker import Faker


class TestCreateMenu(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('menu:store')
        self.faker = Faker()

    def test_create_menu_success(self):
        user, token, credentials = self.generate_chef_user()

        self.set_client_credentials(token)

        response = self.client.post(self.route, {
            'day': str(self.faker.future_date()),
            'options': [
                'Pastel de choclo, Ensalada y Postre',
                'Arroz con nugget de pollo, Ensalada y Postre',
                'Arroz con hamburguesa, Ensalada y Postre',
            ]
        }, format='json')

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_error_when_trying_to_create_menu_with_unauthorized_profile(self):
        user, token, credentials = self.generate_employee_user()

        self.set_client_credentials(token)

        response = self.client.post(self.route, {
            'day': str(self.faker.future_date()),
            'options': [
                'Pastel de choclo, Ensalada y Postre',
                'Arroz con nugget de pollo, Ensalada y Postre',
                'Arroz con hamburguesa, Ensalada y Postre',
            ]
        }, format='json')

        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_try_to_create_two_menus_for_the_same_day(self):
        user, token, credentials = self.generate_chef_user()

        self.set_client_credentials(token)

        day_menu = self.faker.future_date()

        Menu.objects.create(user=user, day=day_menu)

        response = self.client.post(self.route, {
            'day': str(day_menu),
            'options': [
                'Pastel de choclo, Ensalada y Postre',
                'Arroz con nugget de pollo, Ensalada y Postre',
                'Arroz con hamburguesa, Ensalada y Postre',
            ]
        }, format='json')

        self.assertTrue(response.status_code, HTTP_400_BAD_REQUEST)
