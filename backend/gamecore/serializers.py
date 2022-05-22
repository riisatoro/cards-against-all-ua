from rest_framework.serializers import ModelSerializer, Serializer, CharField

from gamecore.models import RoomModel


class DefaultResponseSerializer(Serializer):
    detail = CharField()

    class Meta:
        fields = ('detail',)


class CreateRoomSerializer(ModelSerializer):

    class Meta:
        model = RoomModel
        fields = ('is_private', )
