from rest_framework.generics import ListAPIView
from cornerapps.menu.models import Menu
from cornerapps.menu.serializers import IndexMenuModelSerializer


class IndexMenu(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = IndexMenuModelSerializer
