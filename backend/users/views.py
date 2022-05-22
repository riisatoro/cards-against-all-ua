from django.contrib.auth.hashers import make_password
from rest_framework.generics import CreateAPIView

from authentication.models import User
from users.serializers import CreateUserSerializer, SaveUserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    authentication_classes = []

    def perform_create(self, serializer):
        user = SaveUserSerializer(
            data={
                **serializer.data,
                'password': make_password(serializer.data['password'])
            }
        )
        if user.is_valid():
            user.save()
