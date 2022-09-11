from django.contrib.auth.hashers import make_password
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response


from users.serializers import CreateUserSerializer, SaveUserSerializer, UserSerializer


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

@extend_schema(
    tags=('User',),
    responses={
        200: UserSerializer,
    }
)
class UserDataView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data, 200)
