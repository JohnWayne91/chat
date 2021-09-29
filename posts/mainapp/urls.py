from django.urls import path

from .views import PostListView, PostDetailView, CommentCreateView, SignInUser, RegisterUser, logout_user

urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('posts/<str:post_slug>/', PostDetailView.as_view(), name='post'),
    path('create/', CommentCreateView.as_view(), name='comment-create'),
    path('sign_in/', SignInUser.as_view(), name='sign_in'),
    path('sign_up/', RegisterUser.as_view(), name='sign_up'),
    path('logout/', logout_user, name='logout'),
]
