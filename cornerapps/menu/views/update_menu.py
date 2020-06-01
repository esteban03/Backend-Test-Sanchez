from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from cornerapps.user.permissions import IsChef
from cornerapps.menu.serializers import MenuModelSerializer
from cornerapps.menu.models import Menu


class UpdateMenu(UpdateAPIView):
    permission_classes = (IsAuthenticated, IsChef, )
    queryset = Menu.objects.all()
    serializer_class = MenuModelSerializer
    lookup_field = 'id'

