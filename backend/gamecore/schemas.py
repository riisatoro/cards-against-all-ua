from rest_framework.serializers import (
    BooleanField,
    CharField,
    Serializer,
)


class CreateRoomSchema(Serializer):
    is_private = BooleanField(default=False)

    class Meta:
        fields = ("is_private",)


class JoinRoomSchema(Serializer):
    room_uuid = CharField(max_length=500, required=False)

    class Meta:
        fields = ("room_uuid",)


class DefaultResponseSchema(Serializer):
    detail = CharField()

    class Meta:
        fields = ("detail",)
