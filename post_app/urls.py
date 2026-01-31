from django.contrib import admin
from django.urls import path, include
from .views import AllPosts, PostDetail, PostComments, CommentDetail

urlpatterns = [
    path('posts/', AllPosts.as_view()),
    path('posts/<int:post_id>/', PostDetail.as_view()),
    path('posts/<int:post_id>/comments/', PostComments.as_view()),
    path('posts/<int:post_id>/comments/<int:comment_id>/', CommentDetail.as_view()),
]
