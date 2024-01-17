from channels.generic.websocket import JsonWebsocketConsumer


class RolePlayingConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.count = 0

    def receive_json(self, content, **kwargs):
        self.count += 1
        content['count'] = self.count
        self.send_json(content)