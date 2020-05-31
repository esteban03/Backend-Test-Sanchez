from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from cornerapps.user.serializers import UserEmployeeSerializer


class StoreEmployee(CreateAPIView):
    permission_classes = (IsAuthenticated, IsAdminUser)
    serializer_class = UserEmployeeSerializer
