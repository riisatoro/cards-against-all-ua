from rest_framework.serializers import ModelSerializer, CharField
from rest_framework.validators import ValidationError

from authentication.models import User


class CreateUserSerializer(ModelSerializer):
    repeat_password = CharField(required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise ValidationError(detail='Passwords don\'t match')
        return super().validate(attrs)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'repeat_password',)


class SaveUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)
