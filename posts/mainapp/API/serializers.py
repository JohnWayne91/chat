from rest_framework import serializers

from ..models import Posts, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('comments',)


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Posts
        fields = '__all__'

    def create(self, validated_data):
        comments_data = validated_data.pop('comments')
        post = Posts.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(related_post=post, **comment_data)
        return post
