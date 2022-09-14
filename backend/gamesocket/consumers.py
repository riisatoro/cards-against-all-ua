import json
from channels.generic.websocket import WebsocketConsumer


class GameRoomNotifications(WebsocketConsumer):
    def connect(self):
        user = self.scope['user']
        room_id = self.scope["url_route"]["kwargs"]["room_id"]

        if user.is_authenticated:
            self.accept()
        else:
            self.close()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        self.send(text_data=json.dumps({"message": message}))
