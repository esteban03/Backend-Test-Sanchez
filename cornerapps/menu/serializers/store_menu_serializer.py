from rest_framework import serializers
from cornerapps.menu.models import Menu, Option


class StoreMenuSerializer(serializers.Serializer):
    day = serializers.DateField()
    options = serializers.ListField(
        child=serializers.CharField(max_length=250)
    )

    def create(self, validated_data):
        auth_user = self.context['request'].user
        menu = Menu.objects.create(user=auth_user, day=validated_data['day'])

        for option in validated_data['options']:
            Option.objects.create(menu=menu, description=option)

        return {
            'day': menu.day,
            'options': [option.description for option in menu.options.all()],
        }
