import json
from channels.generic.websocket import WebsocketConsumer


class GameRoomNotifications(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        self.room_id = self.scope["url_route"]["kwargs"]["room_id"]

        if user.is_authenticated:
            self.accept()
            self.channel_layer.group_add(self.room_id, self.channel_name)
        else:
            self.close()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.room_id, self.channel_name)
        self.close()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.send(text_data=json.dumps({"message": message}))
