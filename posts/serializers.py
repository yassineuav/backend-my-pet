from rest_framework import serializers

from posts.models import Like, Post, Collection, Product


class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "likes_count"]

    def create(self, validated_data):
        post = Post(**validated_data)
        post.other = 1
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.save()
        return instance

    # def validate(self, data):
    #     if data['title'] == data['description']:
    #         return serializers.ValidationError('title and description has to be not matched idiots!')
    #     return data


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)


class CollectionProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    collection = CollectionProductSerializer()

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'collection']
