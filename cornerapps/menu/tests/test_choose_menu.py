import datetime

from django.urls import reverse

from rest_framework.test import APIRequestFactory
from rest_framework.exceptions import PermissionDenied

from shared.tests import ApiTestCaseBase
from cornerapps.menu.models import Menu, Option
from cornerapps.menu.serializers import StoreChooseMenuSerializer

from faker import Faker


class TestChooseMenu(ApiTestCaseBase):

    def setUp(self):
        self.route = reverse('menu:store.choose')
        self.faker = Faker()
        self.today_before_11am = datetime.datetime(2020, 6, 22, 10, 0, 0)
        self.today_after_11am = datetime.datetime(2020, 6, 22, 12, 0, 0)

    def test_unit_choose_menu_success(self):
        user, token, credentials = self.generate_employee_user()

        factory = APIRequestFactory()

        menu, options = self.create_menu(user)

        option = options.pop()

        choose = {
            'menu': menu.id,
            'option': option.id,
            'comments': 'Sin aceite'
        }

        request = factory.post(self.route, choose, format='json')
        request.user = user

        serializer = StoreChooseMenuSerializer(data=choose, context={
            'request': request,
            'datetime_now': self.today_before_11am
        })
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def test_unit_choose_menu_after_11am(self):
        user, token, credentials = self.generate_employee_user()

        factory = APIRequestFactory()

        menu, options = self.create_menu(user)

        option = options.pop()

        choose = {
            'menu': menu.id,
            'option': option.id,
            'comments': 'Sin aceite'
        }

        request = factory.post(self.route, choose, format='json')
        request.user = user

        serializer = StoreChooseMenuSerializer(data=choose, context={
            'request': request,
            'datetime_now': self.today_after_11am
        })

        with self.assertRaises(PermissionDenied):
            serializer.is_valid(raise_exception=True)

    def create_menu(self, user):
        today = self.today_before_11am.date()

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
