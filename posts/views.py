from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_405_METHOD_NOT_ALLOWED, HTTP_201_CREATED
from rest_framework.views import APIView


from .models import Post, Collection, Product
from .serializers import PostSerializer, CollectionSerializer, ProductSerializer


class ProductList(APIView):
    def get(self, request):
        queryset = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(data=serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(data=serializer.data, status=HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        queryset = Post.objects.annotate(likes_count=Count('likes')).all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        if post.likes_count() > 0:
            return Response(data={"error": "cannot delete post with likes"},
                            status=HTTP_405_METHOD_NOT_ALLOWED)
        post.delete()
        return Response(data={"message": f"post title '{post.title}' title delete successful"},
                        status=HTTP_204_NO_CONTENT)


@api_view()
def collection_list(request):
    collection = Collection.objects.annotate(products_count=Count('product')).all()
    serializer = CollectionSerializer(collection, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def collection_detail(request, pk):
    collection = get_object_or_404(Collection, pk=pk)
    if request.method == 'GET':
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)
    elif request.method == 'PUT':
        return Response(f"ok {pk}")