from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post
from .serializers import PostSerializer


@api_view()
def post_list(request):
    posts = Post.objects.all()
    post_serializers = PostSerializer(posts, many=True)
    return Response(post_serializers.data)


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
