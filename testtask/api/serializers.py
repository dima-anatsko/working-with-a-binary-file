from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token

UserModel = get_user_model()


class AuthSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self._data = {}

    def get_user(self):
        return self.user

    def save(self, **kwargs):
        token, _ = Token.objects.get_or_create(user=self.get_user())
        self._data['key'] = token.key


class LoginSerializer(AuthSerializer):
    def validate(self, data):
        self.user = UserModel.objects.filter(username=data['username']).first()
        if not self.user or not self.user.check_password(data['password']):
            raise serializers.ValidationError('Invalid credentials')
        return data


class SignUpSerializer(AuthSerializer):
    def get_user(self):
        return UserModel.objects.create_user(**self.validated_data)
