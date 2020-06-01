from rest_framework.test import APITestCase
from faker import Faker

from cornerapps.user.serializers import AuthLoginSerializer
from cornerapps.user.models import User
from cornerapps.user.serializers import (
    UserEmployeeSerializer,
    UserChefSerializer,
)


class ApiTestCaseBase(APITestCase):
    """
    Base testcase with utilities to test the rest of the project apis
    """

    def get_token_auth(self, credentials):
        """
        Get or create token authentication for tests
        :param credentials: Dict{username, password}
        :return: token str
        """
        serializer = AuthLoginSerializer(data=credentials)
        serializer.is_valid()
        user, token = serializer.save()
        return token

    def generate_credentials(self):
        faker = Faker()
        return {
            'username': faker.email(),
            'password': faker.password()
        }

    def generate_data_user(self):
        faker = Faker()
        email = faker.email(),
        return {
            'username': email,
            'password': faker.password(),
            'first_name': faker.first_name(),
            'last_name': faker.last_name(),
            'email': email
        }

    def generate_admin_user(self):
        """:rtype: tuple(user, token, dict(credentials))"""
        credentials = self.generate_credentials()

        new_user = User.objects.create_user(**credentials, is_staff=True)
        token = self.get_token_auth(credentials)

        return new_user, token, credentials

    def generate_chef_user(self):
        """:rtype: tuple(user, token, dict(credentials))"""
        credentials = self.generate_credentials()
        serializer = UserChefSerializer(data=credentials)
        serializer.is_valid()
        new_user = serializer.save()

        token = self.get_token_auth(credentials)

        return new_user, token, credentials

    def generate_employee_user(self):
        """:rtype: tuple(user, token, dict(credentials))"""
        credentials = self.generate_credentials()
        serializer = UserEmployeeSerializer(data=credentials)
        serializer.is_valid()
        new_user = serializer.save()

        token = self.get_token_auth(credentials)

        return new_user, token, credentials

    def set_client_credentials(self, token):
        """Set credentials for auth api in client object"""
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token))
