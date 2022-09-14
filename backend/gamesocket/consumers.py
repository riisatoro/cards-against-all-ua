import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class GameRoomNotifications(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]

        if user.is_authenticated:
            self.accept()
            async_to_sync(self.channel_layer.group_add)(self.room_id, self.channel_name)
        else:
            self.close()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.room_id, self.channel_name)
        self.close()

    def send_game_info(self, data):
        self.send(text_data=json.dumps(data['data']))
