from channels.generic.websocket import JsonWebsocketConsumer


class RolePlayingConsumer(JsonWebsocketConsumer):
    # def connect(self):
    #     self.accept()

    def receive_json(self, content, **kwargs):
        self.send_json(content)