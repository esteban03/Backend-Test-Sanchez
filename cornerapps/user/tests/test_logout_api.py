from django.urls import reverse

from rest_framework.status import HTTP_200_OK
from rest_framework.authtoken.models import Token

from shared.tests import ApiTestCaseBase


class TestLogoutApi(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('user:auth.logout')

    def test_logout_success(self):
        user, token, credentials = self.generate_admin_user()

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

        response = self.client.post(self.route)

        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_token_after_logout_does_not_exist(self):
        user, token, credentials = self.generate_admin_user()

        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))

        self.client.post(self.route)

        token_exist = Token.objects.filter(user=user).exists()

        self.assertFalse(token_exist)
