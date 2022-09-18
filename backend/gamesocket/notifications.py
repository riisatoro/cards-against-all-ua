from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def notify_room_members(group_id, data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        group_id, {"type": "send_game_data", "data": data}
    )
