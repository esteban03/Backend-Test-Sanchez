from django.urls import reverse

from rest_framework.status import HTTP_201_CREATED, HTTP_403_FORBIDDEN

from shared.tests import ApiTestCaseBase


class TestCreateChefUser(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('user:store.chef')

    def test_create_success_chef_user(self):
        user, token, credentials = self.generate_admin_user()

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

        response = self.client.post(
            self.route,
            self.generate_data_user()
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_employee_with_unauthorized_user(self):
        user, token, credentials = self.generate_chef_user()

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

        response = self.client.post(
            self.route,
            self.generate_data_user()
        )

        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
