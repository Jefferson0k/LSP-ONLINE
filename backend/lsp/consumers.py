import json
from channels.generic.websocket import AsyncWebsocketConsumer

class RecognitionConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        word = data.get('word')
        await self.send(text_data=json.dumps({'word': word}))
