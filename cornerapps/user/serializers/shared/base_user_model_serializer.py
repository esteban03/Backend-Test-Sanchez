from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from cornerapps.user.models import User


class BaseUserModelSerializer(serializers.ModelSerializer):
    """Use it to create serializers of users with specific profile"""

    def validate_password(self, value):
        return make_password(value)

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'created_at',
            'updated_at',
        )
        extra_kwargs = {'password': {'write_only': True}}
