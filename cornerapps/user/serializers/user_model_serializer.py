from django.contrib.auth.hashers import make_password

from cornerapps.user.serializers.shared import BaseUserModelSerializer


class UserModelSerializer(BaseUserModelSerializer):

    def validate_password(self, value):
        return make_password(value)

    class Meta(BaseUserModelSerializer.Meta):
        pass
