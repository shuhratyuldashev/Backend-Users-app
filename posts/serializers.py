from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "image",
            "content",
            "likes",
            "author",   
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author"]


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = [
            "id",
            "post",
            "author",
            "content",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["author"]
