from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from cornerapps.user.serializers.user_model_serializer import UserModelSerializer
from rest_framework.exceptions import AuthenticationFailed


class AuthLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['username'], password=attrs['password'])

        if not user:
            raise AuthenticationFailed

        """Save for use in self.create method"""
        self.context['user'] = user

        return attrs

    def create(self, validated_data):
        user = self.context['user']
        token, created = Token.objects.get_or_create(user=user)
        return UserModelSerializer(user).data, token.key
