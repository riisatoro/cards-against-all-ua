from django.contrib.auth.hashers import make_password
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView


from users.serializers import CreateUserSerializer, SaveUserSerializer


@extend_schema(tags=('User',))
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
