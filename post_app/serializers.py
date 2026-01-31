from rest_framework import serializers
from .models import Posts, Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ("text", "comment_author", "date_created")


class PostsSerializer(serializers.ModelSerializer):
    # this tells the serializer that there could be many comments for each Post
    comments = CommentsSerializer(many=True)

    class Meta:
        model = Posts
        fields = ("title", "post_author", "date_created", "body", "comments")
        # comments are accesed via the related_name we setup in models

# endpoint for retrieving comments of a specific post

