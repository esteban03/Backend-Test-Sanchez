from django.utils import timezone
from datetime import time

from rest_framework import serializers, exceptions

from cornerapps.menu.models import Choose, Option, Menu


class StoreChooseMenuSerializer(serializers.Serializer):
    menu = serializers.PrimaryKeyRelatedField(queryset=Menu.objects.all())
    option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all())
    comments = serializers.CharField(max_length=250, required=False)

    def validate(self, attrs):
        """
        Validate that an option is chosen from today's menu
        Validate that the option belongs to the menu
        """

        option = attrs['option']
        menu = attrs['menu']

        if option.menu_id != menu.id:
            raise exceptions.PermissionDenied(detail="The option does not belong on the menu")

        """The datetime_now parameter is allowed to be sent in context for testability reasons"""
        datetime_now = self.context.get('datetime_now')
        if datetime_now is None:
            datetime_now = timezone.now()

        menu_of_the_day = option.menu.day == datetime_now.date()

        if not menu_of_the_day:
            raise exceptions.PermissionDenied(detail="Not menu of the day")

        after_11AM = datetime_now.time() > time(11, 0, 0)

        if after_11AM:
            raise exceptions.PermissionDenied(detail="Out of time")

        return attrs

    def create(self, validated_data):
        auth_user = self.context['request'].user

        validated_data['user'] = auth_user

        return Choose.objects.create(**validated_data)
