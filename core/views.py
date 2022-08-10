from django.db.models import Count
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from .serializers import UserSerializer, ProfileSerializer, InterestedInSerializer, AddressSerializer, \
    WritePostSerializer, PostsSerializer, LikesSerializer
from .models import InterestedIn, Post, User, Address, Like


class ProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (user, created) = User.objects.get_or_create(id=request.user.id)
        if request.method == 'GET':
            serializer = ProfileSerializer(user)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProfileSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class AddressViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        (address, created) = Address.objects.get_or_create(user_id=request.user.id)
        if request.method == 'GET':
            serializer = AddressSerializer(address)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = AddressSerializer(address, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)


class UserAPIView(RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class InterestedInViewSet(viewsets.ModelViewSet):
    queryset = InterestedIn.objects.all()
    serializer_class = InterestedInSerializer
    # permission_classes = [permissions.IsAuthenticated]


class LikesViewSet(ModelViewSet):
    queryset = Like.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            # return WriteLikesSerializer
            return LikesSerializer
        else:
            return LikesSerializer


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # queryset = Post.objects.select_related('likes').all()
    queryset = Post.objects.annotate(likes_count=Count('likes')).all()
    #
    # def get_queryset(self):
    #     user = self.request.user

    #     if user.is_staff:
    #         return Post.objects.all()
    #     return Post.objects.filter(user_id=user.id)

    def get_serializer_class(self):
        if self.request.method == 'PUT' or self.request.method == 'POST':
            return WritePostSerializer
        else:
            return PostsSerializer


class MyPostViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = WritePostSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(user_id=user.id)


