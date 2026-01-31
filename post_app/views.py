from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Posts, Comments
from .serializers import PostsSerializer, CommentsSerializer


class AllPosts(APIView):
    def get(self, request):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get(self, request, post_id):
        post = Posts.objects.get(post_id=post_id)
        serializer = PostsSerializer(post)
        return Response(serializer.data)


class PostComments(APIView):
    def get(self, request, post_id):
        comments = Comments.objects.filter(post=post_id)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)


class CommentDetail(APIView):
    def get(self, request, post_id, comment_id):
        comment = Comments.objects.get(id=comment_id, post=post_id)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)
