from rest_framework.permissions import BasePermission
from cornerapps.user.models import UserProfileEmployee


class IsEmployee(BasePermission):

    def has_permission(self, request, view):
        is_employee_user = UserProfileEmployee.objects.filter(user=request.user).exists()
        return is_employee_user
