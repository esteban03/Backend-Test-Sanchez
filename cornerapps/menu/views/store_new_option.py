from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from cornerapps.user.permissions import IsChef
from cornerapps.menu.serializers import OptionModelSerializer


class StoreNewOption(CreateAPIView):
    permission_classes = (IsAuthenticated, IsChef,)
    serializer_class = OptionModelSerializer
