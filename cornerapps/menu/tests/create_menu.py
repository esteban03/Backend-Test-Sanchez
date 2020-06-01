from django.urls import reverse

from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

from shared.tests import ApiTestCaseBase
from cornerapps.user.serializers import UserChefSerializer, UserEmployeeSerializer

from faker import Faker


class TestCreateMenu(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('menu:store')
        self.faker = Faker()

    def test_create_menu_success(self):
        user, token = self.generate_chef_user()

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

        response = self.client.post(self.route, {
            'day': str(self.faker.future_date()),
            'options': [
                'Pastel de choclo, Ensalada y Postre',
                'Arroz con nugget de pollo, Ensalada y Postre',
                'Arroz con hamburguesa, Ensalada y Postre',
            ]
        })

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_error_when_trying_to_create_menu_with_unauthorized_profile(self):
        user, token = self.generate_employee_user()

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

        response = self.client.post(self.route, {
            'day': str(self.faker.future_date()),
            'options': [
                'Pastel de choclo, Ensalada y Postre',
                'Arroz con nugget de pollo, Ensalada y Postre',
                'Arroz con hamburguesa, Ensalada y Postre',
            ]
        })

        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
