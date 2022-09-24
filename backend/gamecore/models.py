from uuid import uuid4

from django.db.models import (
    BooleanField,
    CASCADE,
    CharField,
    DateTimeField,
    IntegerField,
    PositiveIntegerField,
    ForeignKey,
    ManyToManyField,
    SET_NULL,
    UUIDField,
    IntegerChoices,
)
from django.db.models import Model as Base

from authentication.models import User


class Model(Base):
    id = UUIDField(default=uuid4, primary_key=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GameState(IntegerChoices):
    WAIT_FOR_NEW_PLAYERS = (0, "Wait for new players")
    WAIT_FOR_NEW_ROUND = (1, "Wait for new round")
    WAIT_FOR_USERS_ANSWER = (2, "Wait for users answer")
    WAIT_FOR_LEADER_SELECT = (3, "Wait for leader select")
    GAME_ENDED = (4, "Game finished")


class CardModel(Model):
    QUESTION = "question"
    ANSWER = "answer"
    CARD_TYPES = (
        (ANSWER, "Answer"),
        (QUESTION, "Question"),
    )

    text = CharField(max_length=255)
    card_type = CharField(max_length=100, choices=CARD_TYPES)
    answers_amount = IntegerField(default=1)

    def __str__(self):
        return f"[{self.id}] {self.card_type}: {self.text}"


class RoomModel(Model):
    room_state = IntegerField(
        default=GameState.WAIT_FOR_NEW_PLAYERS, choices=GameState.choices
    )
    is_private = BooleanField(default=False)

    round_number = PositiveIntegerField(default=0)
    round_end_time = DateTimeField(auto_now_add=True)

    leader = ForeignKey(
        to=User, on_delete=SET_NULL, null=True, blank=True, related_name="leader"
    )
    users = ManyToManyField(to=User, related_name="users")

    question_card = ForeignKey(
        to="CardModel",
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name="question_card",
    )
    round_winner = ForeignKey(
        to="authentication.User",
        on_delete=SET_NULL,
        null=True,
        blank=True,
        related_name="round_winner",
    )

    class Meta:
        ordering = ("room_state",)
