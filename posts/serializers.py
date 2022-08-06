from rest_framework import serializers

from posts.models import Like, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "description", "likes_count"]