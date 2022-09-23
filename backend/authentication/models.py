from django.contrib.auth.models import AbstractUser
from django.db.models import ManyToManyField, EmailField, IntegerField


class User(AbstractUser):
    email = EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    cards = ManyToManyField(
        to="gamecore.CardModel", null=True, blank=True, related_name="cards"
    )
    answer_cards = ManyToManyField(
        to="gamecore.CardModel", null=True, blank=True, related_name="answers"
    )
    score = IntegerField(default=0)
