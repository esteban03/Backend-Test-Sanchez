from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cornerapps.menu.models import Menu, Option


class StoreMenuSerializer(serializers.Serializer):
    day = serializers.DateField()
    options = serializers.ListField(
        child=serializers.CharField(max_length=250)
    )

    def validate_day(self, value):

        exist_menu_for_day = Menu.objects.filter(day=value).exists()

        if exist_menu_for_day:
            raise serializers.ValidationError(detail="There is a menu for the day {}".format(value))

        return value

    def create(self, validated_data):
        auth_user = self.context['request'].user
        menu = Menu.objects.create(user=auth_user, day=validated_data['day'])

        for option in validated_data['options']:
            Option.objects.create(menu=menu, description=option)

        return {
            'day': menu.day,
            'options': [option.description for option in menu.options.all()],
        }
