from datetime import date, datetime, time

from rest_framework import serializers, exceptions

from cornerapps.menu.models import Choose, Option


class ChooseMenuSerializer(serializers.Serializer):
    option = serializers.PrimaryKeyRelatedField(queryset=Option.objects.all())
    comments = serializers.CharField(max_length=250, required=False)

    def validate(self, attrs):
        """Validate that an option is chosen from today's menu at a valid time"""

        option = attrs['option']

        menu_is_today = option.menu.day == date.today()

        if not menu_is_today:
            raise exceptions.PermissionDenied(detail="Not the menu of the day")

        is_it_past_11_in_the_morning = datetime.now().time() > time(11, 0, 0)

        if is_it_past_11_in_the_morning:
            raise exceptions.PermissionDenied(detail="Out of time")

        return attrs

    def create(self, validated_data):
        auth_user = self.context['request'].user

        validated_data['user'] = auth_user

        return Choose.objects.create(**validated_data)
