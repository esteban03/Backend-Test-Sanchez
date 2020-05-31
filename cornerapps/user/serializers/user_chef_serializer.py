from cornerapps.user.models import UserProfileChef
from cornerapps.user.serializers.shared import BaseUserModelSerializer


class UserChefSerializer(BaseUserModelSerializer):

    def create(self, validated_data):
        user = super(UserChefSerializer, self).create(validated_data)
        UserProfileChef.objects.create(user=user)
        return user

    class Meta(BaseUserModelSerializer.Meta):
        pass
