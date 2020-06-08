from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from cornerapps.menu.models import Menu
from cornerapps.menu.serializers import IndexMenuModelSerializer
from cornerapps.user.permissions import IsChef

from django_filters.rest_framework import DjangoFilterBackend


class IndexMenu(ListAPIView):
    permission_classes = (IsAuthenticated, IsChef, )
    queryset = Menu.objects.all()
    serializer_class = IndexMenuModelSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_fields = ('day', )
