from cornerapps.user.models import UserProfileEmployee
from cornerapps.user.serializers.shared import BaseUserModelSerializer


class UserEmployeeSerializer(BaseUserModelSerializer):

    def create(self, validated_data):
        user = super(UserEmployeeSerializer, self).create(validated_data)
        UserProfileEmployee.objects.create(user=user)
        return user

    class Meta(BaseUserModelSerializer.Meta):
        pass
