from django.contrib import admin

from gamecore.models import (
    CardModel,
    RoomModel,
    UserRoomModel,
)


@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ('text', 'card_type',)
    list_filter = ('card_type',)


@admin.register(RoomModel)
class RoomModelAdmin(admin.ModelAdmin):
    list_display = (
        'is_started', 'is_ended', 'is_private',
        'round_number', 'round_end_time',
        'leader',
        'question_card', 'best_answer_card',
    )


@admin.register(UserRoomModel)
class UserRoomModelAdmin(admin.ModelAdmin):
    list_display = ('room', 'user', 'score',)
    filter_horizontal = ('answer', 'cards',)
