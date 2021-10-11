from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.filters import SearchFilter

from .serializers import PostSerializer, CommentSerializer
from ..models import Posts, Comment


class PostListApiView(ListAPIView, ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id', 'title']


class PostDetailApiView(RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    lookup_field = 'id'


class CommentsListApiView(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    # lookup_field = 'related_post'
    filter_backends = [SearchFilter]
    search_fields = ['related_post__title']
