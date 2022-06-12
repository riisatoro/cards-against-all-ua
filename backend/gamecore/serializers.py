from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    Serializer,
)

from authentication.models import User
from gamecore.models import (
    CardModel,
    RoomModel,
    UserRoomModel,
)


class DefaultResponseSerializer(Serializer):
    detail = CharField()

    class Meta:
        fields = ('detail',)


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class CreateRoomSerializer(ModelSerializer):

    class Meta:
        model = RoomModel
        fields = ('is_private', )


class CardSerializer(ModelSerializer):

    class Meta:
        model = CardModel
        fields = ('id', 'text', 'card_type',)


class UserRoomSerializer(ModelSerializer):
    answer = CardSerializer()
    cards = CardSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = UserRoomModel
        fields = ('user', 'score', 'answer', 'cards')


class RoomSerializer(ModelSerializer):
    best_answer_card = CardSerializer()
    question_card = CardSerializer()
    leader = UserRoomSerializer()
    users = UserRoomSerializer(source='userroommodel_set', many=True)

    class Meta:
        model = RoomModel
        fields = (
            'id', 'is_private', 'is_started', 'is_ended',
            'round_number', 'leader', 'question_card',
            'best_answer_card', 'users',
        )


class JoinRoomSerializer(Serializer):
    room_uuid = CharField(max_length=500, required=False)
