from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    Serializer,
)

from gamecore.models import (
    CardModel,
    RoomModel,
    User,
)





class CardSerializer(ModelSerializer):
    class Meta:
        model = CardModel
        fields = (
            "id",
            "text",
        )


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class PlayerDataSerializer(ModelSerializer):
    cards = CardSerializer(many=True, read_only=True)
    answer_cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = (
            "username",
            "score",
            "cards",
            "answer_cards",
        )


class RoomSerializer(ModelSerializer):
    users = PlayerDataSerializer(many=True, read_only=True)
    leader = PlayerSerializer()

    class Meta:
        model = RoomModel
        fields = (
            "id",
            "is_started",
            "is_ended",
            "round_number",
            "round_end_time",
            "leader",
            "users",
        )
