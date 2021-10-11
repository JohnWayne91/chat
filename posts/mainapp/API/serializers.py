from rest_framework import serializers

from ..models import Posts, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = '__all__'
