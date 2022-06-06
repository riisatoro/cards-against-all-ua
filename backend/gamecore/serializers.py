from ast import Mod
from attr import fields_dict
from rest_framework.serializers import ModelSerializer, Serializer, CharField
from authentication.models import User

from gamecore.models import RoomModel, CardModel, UserRoomModel


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
    users = UserRoomSerializer(source='userroommodel_set', many=True)

    class Meta:
        model = RoomModel
        fields = (
            'id', 'is_private', 'is_started', 'is_ended',
            'round_number', 'leader', 'question_card',
            'best_answer_card', 'users',
        )
