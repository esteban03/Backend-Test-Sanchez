from rest_framework import serializers

from cornerapps.menu.models import Menu


class IndexMenuModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'id',
            'day',
            'options',
        )
        depth = 1
