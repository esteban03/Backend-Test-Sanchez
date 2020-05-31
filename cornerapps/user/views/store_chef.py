from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.generics import CreateAPIView
from cornerapps.user.serializers import UserChefSerializer


class StoreChef(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = UserChefSerializer
