from rest_framework.permissions import BasePermission

from cornerapps.menu.exceptions import BadRequest
from cornerapps.menu.models import Option


class AuthorizedScheduleToChoose(BasePermission):
    message = "Menu closed"

    def has_permission(self, request, view):
        try:
            options_pk = request['option']
            option = Option.objects.get(pk=options_pk)
            breakpoint()

        except BaseException:
            raise BadRequest

