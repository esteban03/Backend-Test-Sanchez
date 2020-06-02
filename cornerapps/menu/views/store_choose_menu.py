from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from cornerapps.user.permissions import IsEmployee
from cornerapps.menu.serializers import ChooseMenuSerializer
from cornerapps.menu.permissions import AuthorizedScheduleToChoose

class StoreChooseMenu(CreateAPIView):
    permission_classes = (IsAuthenticated, IsEmployee, )
    serializer_class = ChooseMenuSerializer
