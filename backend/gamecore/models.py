from uuid import uuid4

from django.db.models import (
    BooleanField,
    CASCADE,
    CharField,
    DateTimeField,
    PositiveIntegerField,
    ForeignKey,
    ManyToManyField,
    SET_NULL,
    UUIDField,
)
from django.db.models import Model as Base

from authentication.models import User


class Model(Base):
    id = UUIDField(default=uuid4, primary_key=True)

    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class CardModel(Model):
    QUESTION = "question"
    ANSWER = "answer"
    CARD_TYPES = (
        (ANSWER, "Answer"),
        (QUESTION, "Question"),
    )

    text = CharField(max_length=255)
    card_type = CharField(max_length=100, choices=CARD_TYPES)

    def __str__(self):
        return f"[{self.id}] {self.card_type}: {self.text}"


class RoomModel(Model):
    is_started = BooleanField(default=False)
    is_ended = BooleanField(default=False)
    is_private = BooleanField(default=False)

    round_number = PositiveIntegerField(default=0)
    round_end_time = DateTimeField(auto_now_add=True)

    leader = ForeignKey(to=User, on_delete=SET_NULL, null=True, blank=True, related_name="leader")
    users = ManyToManyField(to=User, related_name="users")

    question_card = ForeignKey(
        to="CardModel", on_delete=SET_NULL, null=True, blank=True, related_name="question_card"
    )
    best_answer_card = ForeignKey(
        to="CardModel", on_delete=SET_NULL, null=True, blank=True, related_name="best_answer_card"
    )

    class Meta:
        ordering = ('-is_started', )
