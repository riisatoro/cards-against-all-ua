from django.contrib import admin

from gamecore.models import (
    CardModel,
    RoomModel,
)


@admin.register(CardModel)
class CardModelAdmin(admin.ModelAdmin):
    list_display = (
        "text",
        "card_type",
    )
    list_filter = ("card_type",)


@admin.register(RoomModel)
class RoomModelAdmin(admin.ModelAdmin):
    list_display = (
        "is_private",
        "room_state",
        "round_number",
        "round_end_time",
    )
    filter_horizontal = ("users",)
    list_filter = ("room_state",)
