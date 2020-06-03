from rest_framework import serializers

from cornerapps.menu.models import Menu
from cornerapps.menu.serializers import OptionModelSerializer
from cornerapps.menu.models import Option


class MenuModelSerializer(serializers.ModelSerializer):
    options = OptionModelSerializer(many=True, required=False)

    def validate_options(self, value):
        options = self.context['request'].data.get('options')

        """Validate that all options belong to the edited menu"""
        options_pk = [option['id'] for option in options]
        options_menu_count = Option.objects.filter(menu=self.instance, id__in=options_pk).count()

        if len(options) != options_menu_count:
            raise serializers.ValidationError('one or more options does not belong on the menu')

        return value

    def update(self, instance, validated_data):

        options = self.context['request'].data.get('options')

        if options is not None:
            for option in options:
                Option.objects.filter(pk=option['id']).update(description=option['description'])

        instance.day = validated_data['day']
        instance.save()

        return instance

    class Meta:
        model = Menu
        fields = (
            'id',
            'day',
            'options',
            'created_at',
            'updated_at',
        )
