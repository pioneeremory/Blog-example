from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Posts, Comments
from .serializers import PostsSerializer, CommentsSerializer


class AllPosts(APIView):
    def get(self, request, post_id):
        posts = Posts.objects.all()
        serializer = PostsSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class PostDetail(APIView):
    def get(self, request, post_id):
        post = Posts.objects.get(id=post_id)
        serializer = PostsSerializer(post)
        return Response(serializer.data)

    def put(self, request, post_id):
        post = Posts.objects.get(id=post_id)
        request.data["id"] = post_id
        serializer = PostsSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, post_id):
        post = Posts.objects.get(id=post_id)
        post.delete()
        return Response({"message": "Post deleted."})


class PostComments(APIView):
    def get(self, request, post_id):
        comments = Comments.objects.filter(post_id=post_id)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, post_id):
        request.data["post"] = post_id
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class CommentDetail(APIView):
    def get(self, request, post_id, comment_id):
        comment = Comments.objects.get(id=comment_id, post=post_id)
        serializer = CommentsSerializer(comment)
        return Response(serializer.data)

    def put(self, request, post_id, comment_id):
        comment = Comments.objects.get(id=comment_id, post=post_id)
        request.data["id"] = comment_id
        request.data["post"] = post_id
        serializer = CommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, post_id, comment_id):
        comment = Comments.objects.get(id=comment_id)
        comment.delete()
        return Response({"message": "Comment deleted."})
