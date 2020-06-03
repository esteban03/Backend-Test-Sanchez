from django.utils import timezone
from datetime import time

from rest_framework import serializers, exceptions

from cornerapps.menu.models import Choose, Option


class ChooseMenuSerializer(serializers.Serializer):
    option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all())
    comments = serializers.CharField(max_length=250, required=False)

    def validate(self, attrs):
        """Validate that an option is chosen from today's menu"""

        option = attrs['option']

        """Time is allowed to be sent in context for testability reasons"""
        datetime_now = self.context.get('datetime_now')
        if datetime_now is None:
            datetime_now = timezone.now()

        menu_is_today = option.menu.day == datetime_now.date()

        if not menu_is_today:
            raise exceptions.PermissionDenied(detail="Not the menu of the day")

        after_11am = datetime_now.time() > time(11, 0, 0)

        if after_11am:
            raise exceptions.PermissionDenied(detail="Out of time")

        return attrs

    def create(self, validated_data):
        auth_user = self.context['request'].user

        validated_data['user'] = auth_user

        return Choose.objects.create(**validated_data)
