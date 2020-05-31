from rest_framework.permissions import BasePermission
from cornerapps.user.models import UserProfileChef


class IsChef(BasePermission):

    def has_permission(self, request, view):
        is_chef_user = UserProfileChef.objects.filter(user=request.user).exists()
        return is_chef_user
