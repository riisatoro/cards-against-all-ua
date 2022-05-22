from rest_framework.generics import CreateAPIView

from authentication.models import User
from users.serializers import CreateUserSerializer


class CreateUserView(CreateAPIView):
    serializer_class = CreateUserSerializer
    authentication_classes = []

    def perform_create(self, serializer):
        data = serializer.data
        data.pop('repeat_password', '')
        User.objects.create(**data, is_active=True)
