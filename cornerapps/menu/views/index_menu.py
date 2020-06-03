from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from cornerapps.menu.models import Menu
from cornerapps.menu.serializers import IndexMenuModelSerializer
from cornerapps.user.permissions import IsChef


class IndexMenu(ListAPIView):
    permission_classes = (IsAuthenticated, IsChef, )
    queryset = Menu.objects.all()
    serializer_class = IndexMenuModelSerializer
