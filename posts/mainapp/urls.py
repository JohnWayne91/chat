from django.urls import path

from .views import PostListView, PostDetailView, CommentCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('posts/<str:post_slug>/', PostDetailView.as_view(), name='post'),
    path('create/', CommentCreateView.as_view(), name='comment-create')
]
