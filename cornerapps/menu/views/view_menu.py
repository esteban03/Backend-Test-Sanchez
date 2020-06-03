from rest_framework.generics import RetrieveAPIView

from cornerapps.menu.models import Menu
from cornerapps.menu.serializers import MenuModelSerializer


class ViewMenu(RetrieveAPIView):
    lookup_field = 'id'
    queryset = Menu.objects.all()
    serializer_class = MenuModelSerializer
