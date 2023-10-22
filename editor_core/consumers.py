from channels.generic.websocket import AsyncWebsocketConsumer
import json

class TrackConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Extract the track ID from the URL or wherever it's provided
        self.track_id = self.scope['url_route']['kwargs']['track_id']

        await self.accept()
        await self.join_track_group()

    async def disconnect(self, close_code):
        await self.leave_track_group()

    async def receive(self, text_data):
        message = text_data
        await self.broadcast_message(message)

    async def broadcast_message(self, message):
        await self.channel_layer.group_send(
            self.track_group_name(),
            {
                "type": "send_message",
                "text": message,
            },
        )

    async def join_track_group(self):
        await self.channel_layer.group_add(self.track_group_name(), self.channel_name)

    async def leave_track_group(self):
        await self.channel_layer.group_discard(self.track_group_name(), self.channel_name)

    async def send_message(self, event):
        text = event['text']
        await self.send(text)

    def track_group_name(self):
        return f"track_{self.track_id}"