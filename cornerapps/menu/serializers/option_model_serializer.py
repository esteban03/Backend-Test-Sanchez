from rest_framework import serializers

from cornerapps.menu.models import Option


class OptionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        read_only_fields = ('id', 'updated_at', 'created_at')
        fields = (
            'id',
            'description',
            'updated_at',
            'created_at',
        )

