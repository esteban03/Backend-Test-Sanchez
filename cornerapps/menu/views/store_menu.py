from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from cornerapps.menu.serializers import StoreMenuSerializer
from cornerapps.user.permissions import IsChef


class StoreMenu(CreateAPIView):
    permission_classes = (IsAuthenticated, IsChef)
    serializer_class = StoreMenuSerializer
