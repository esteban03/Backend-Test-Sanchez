from django.urls import reverse

from rest_framework.status import HTTP_201_CREATED

from shared.tests import ApiTestCaseBase


class TestCreateEmployeeUser(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('user:store.employee')

    def test_create_success_employee(self):
        user, token, credentials = self.generate_admin_user()

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

        response = self.client.post(
            self.route,
            self.generate_data_user()
        )

        self.assertEqual(response.status_code, HTTP_201_CREATED)
