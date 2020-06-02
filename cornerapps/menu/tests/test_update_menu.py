from django.urls import reverse

from rest_framework.status import HTTP_200_OK, HTTP_403_FORBIDDEN

from shared.tests import ApiTestCaseBase
from cornerapps.menu.models import Menu, Option

from faker import Faker


class TestUpdateMenu(ApiTestCaseBase):

    def setUp(self):
        self.faker = Faker()

    def test_update_menu_success(self):
        user, token, credentials = self.generate_chef_user()
        self.set_client_credentials(token)

        menu, options = self.create_menu(user)

        route = reverse('menu:update', kwargs={'id': menu.id})

        day_after_today_update = str(self.faker.future_date())
        update_menu = {'day': day_after_today_update, 'options': []}

        for option in options:
            update_menu['options'].append({
                'id': option.pk,
                'description': 'update food',
            })

        response = self.client.put(route, update_menu, format='json')

        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data['day'], day_after_today_update)
        self.assertEqual(
            response.data['options'][0]['description'],
            update_menu['options'][0]['description'],
        )

    def test_update_menu_with_user_unauthorized(self):
        user, token, credentials = self.generate_employee_user()
        self.set_client_credentials(token)

        menu, new_options = self.create_menu(user)

        route = reverse('menu:update', kwargs={'id': menu.id})

        response = self.client.put(route, format='json')

        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def create_menu(self, user):
        day_after_today = self.faker.future_date()
        options = (
            "Tallerines con helado",
            "Pure con papas fritas",
            "Carne mechada con pure",
        )

        menu = Menu.objects.create(user=user, day=day_after_today)

        new_options = []
        for option in options:
            new_options.append(
                Option.objects.create(menu=menu, description=option)
            )
        return menu, new_options
