import json
<<<<<<< HEAD
import asyncio
=======
>>>>>>> reworking_delay
from datetime import datetime

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
        comment_delay_time_str = text_data_json['comment_time']
        new_comment = await self.create_new_comment(comment, comment_delay_time_str)
        data = {'author': new_comment.author.username,
                'text': new_comment.text,
                'comment_time': new_comment.comment_time.strftime('%Y-%m-%d %H:%M')
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
    def create_new_comment(self, text, comment_delay_time_str):
        post = Posts.objects.get(pk=int(self.post_id))
        if comment_delay_time_str == '':
            new_comment = Comment.objects.create(
                author=self.scope['user'],
                text=text,
                related_post=post,
                comment_time=datetime.now()
            )
        else:
            new_comment = Comment.objects.create(
                author=self.scope['user'],
                text=text,
                related_post=post,
                comment_time=datetime.strptime(comment_delay_time_str, "%m/%d/%Y %H:%M")
            )
        post.comments.add(new_comment)
        return new_comment

