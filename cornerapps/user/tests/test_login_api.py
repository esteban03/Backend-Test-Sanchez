from django.urls import reverse

from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED

from shared.tests import ApiTestCaseBase
from cornerapps.user.serializers import UserModelSerializer


class TestLoginApi(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('user:auth.login')

    def test_success_login(self):
        user, token, credentials = self.generate_admin_user()
        user = UserModelSerializer(user)

        response = self.client.post(self.route, credentials)

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(token, response.data['token'])
        self.assertDictEqual(user.data, response.data['user'])

    def test_error_login(self):
        response = self.client.post(self.route, self.generate_credentials())

        self.assertEqual(response.status_code, HTTP_401_UNAUTHORIZED)
