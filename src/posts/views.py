from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post, Comment
from posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['get'])
    def vote(self, request, pk):
        # Create or updates Votes object, add 1 to amount
        obj, _ = Post.objects.update_or_create(id=pk)
        obj.update_amount()
        return Response(status=status.HTTP_200_OK)


