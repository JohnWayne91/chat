from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.filters import SearchFilter

from .serializers import PostSerializer
from ..models import Posts


class PostListApiView(ListAPIView, ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['id', 'title']


class PostDetailApiView(RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView):
    serializer_class = PostSerializer
    queryset = Posts.objects.all()
    lookup_field = 'id'
