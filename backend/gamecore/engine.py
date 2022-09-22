from random import choice, shuffle
from django.conf import settings

from gamecore.models import RoomModel, CardModel


class GameEngine:
    @staticmethod
    def select_room_leader(room: RoomModel):
        """Set new room leader, excluded previous one"""
        players = room.users.all()

        if current_leader := room.leader:
            players = players.exclude(id=current_leader.id)

        room.leader = choice(players)

    @staticmethod
    def distribute_answer_cards(room: RoomModel):
        distributed_cards = room.userroommodel_set.values_list(
            "cards", flat=True
        ).exclude(cards__isnull=True)

        available_cards = list(
            CardModel.objects.filter(card_type=CardModel.ANSWER).exclude(
                id__in=distributed_cards
            )
        )
        shuffle(available_cards)

        distributed_amount = 0
        for user_room_data in room.userroommodel_set.all():
            cards_amount_to_distribute = (
                settings.DEFAULT_ANSWERS_AMOUNT
                - user_room_data.cards.count()  # if user has 0 cards
                + user_room_data.answer.count()
            )

            user_room_data.cards.add(
                *available_cards[
                    distributed_amount : distributed_amount + cards_amount_to_distribute
                ]
            )

            if answers := list(user_room_data.answer.all()):
                user_room_data.cards.remove(*answers)

            user_room_data.answer.clear()
            distributed_amount += cards_amount_to_distribute

    @staticmethod
    def select_question_card(room: RoomModel):
        return room

    @staticmethod
    def try_start_game(room: RoomModel):
        if room.is_started:
            return False

        if room.users.count() >= settings.MIN_ROOM_PLAYERS:
            room.is_started = True
            # room = GameEngine.select_room_leader(room)
            # room = GameEngine.select_question_card(room)
            # room = GameEngine.distribute_answer_cards(room)

        room.save()
        return True
