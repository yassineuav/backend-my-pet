from django.forms import IntegerField
from rest_framework import serializers
from .models import InterestedIn, Post, User, Address, Like
from djoser.serializers import UserSerializer as BaseUserSerializer,\
    UserCreateSerializer as BaseUserCreateSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user_id', 'street', 'city', 'state', 'zip', 'country']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'imageUrl', 'first_name', 'last_name', 'gender', 'phone', 'bio']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'first_name', 'last_name', 'phone', 'bio', 'imageUrl']


class InterestedInSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = InterestedIn
        fields = '__all__'


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class WriteLikesSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    liked_post_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ['id', 'user_id', 'liked_post_id']


class PostsSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    # likes = serializers.IntegerField()

    # likes_count = Like.objects.filter('liked_post==post.id').Count()

    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'user', 'description', 'imageUrl',
                  'content_type', 'display', 'create_at',
                  'comments', 'likes_count', 'uploaded_from']


class WritePostSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Post
        fields = ['id', 'user_id', 'description', 'imageUrl', 'content_type', 'uploaded_from']


class MyPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
