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
from users.serializers import UserSerializer


class DefaultResponseSerializer(Serializer):
    detail = CharField()

    class Meta:
        fields = ("detail",)


class CreateRoomSerializer(ModelSerializer):
    class Meta:
        model = RoomModel
        fields = ("is_private",)


class CardSerializer(ModelSerializer):
    class Meta:
        model = CardModel
        fields = (
            "id",
            "text",
            "card_type",
        )


class UserRoomSerializer(ModelSerializer):
    answer = CardSerializer(many=True)
    cards = CardSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = UserRoomModel
        fields = ("user", "score", "answer", "cards")


class RoomSerializer(ModelSerializer):
    best_answer_card = CardSerializer()
    question_card = CardSerializer()
    leader = UserRoomSerializer()
    users = UserRoomSerializer(source="userroommodel_set", many=True)

    class Meta:
        model = RoomModel
        fields = (
            "id",
            "is_private",
            "is_started",
            "is_ended",
            "round_number",
            "round_end_time",
            "leader",
            "question_card",
            "best_answer_card",
            "users",
        )


class JoinRoomSerializer(Serializer):
    room_uuid = CharField(max_length=500, required=False)
