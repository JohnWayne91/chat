import json

from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from .models import *


class CommentsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.post_id = self.scope['url_route']['kwargs']['post_id']
        self.post_group_name = 'post_%s' % self.post_id

        # Join room group
        await self.channel_layer.group_add(
            self.post_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.post_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        comment = text_data_json['text']
        new_comment = await self.create_new_comment(comment)
        data = {'author': new_comment.author.username,
                'created_at': new_comment.created_at.strftime('%Y-%m-%d %H:%M'),
                'text': new_comment.text,
                }
        # Send message to room group
        await self.channel_layer.group_send(
            self.post_group_name,
            {
                'type': 'new_comment',
                'message': data
            }
        )

    # Receive message from room group
    async def new_comment(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def create_new_comment(self, text):
        post = Posts.objects.get(pk=int(self.post_id))

        new_comment = Comment.objects.create(
            author=self.scope['user'],
            text=text,
            related_post=post,
        )
        post.comments.add(new_comment)
        return new_comment

