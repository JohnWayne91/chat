from django.urls import path

from .api_views import PostListApiView, PostDetailApiView, CommentsListApiView


urlpatterns = [
    path('posts/', PostListApiView.as_view(), name='posts_list'),
    path('post/<str:id>/', PostDetailApiView.as_view(), name='post_detail'),
    path('comments/', CommentsListApiView.as_view(), name='comments_list')
]