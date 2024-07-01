from django.shortcuts import render
from rest_framework import generics, status
from .models import Post
from .serializers import PostSerializer
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated

class PostListCreateView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    # permission_classes = [IsAuthenticated]

    # for list view, returns posts created by a specific user
    # def get_queryset(self):
    #     user = self.request.user
    #     # if user.is_anonymous:
    #         # raise PermissionDenied('You must be logged in to view posts')
    #     return Post.objects.filter(author=user)

    # for create view
    def perform_create(self, serializer):
        # if not self.request.user.is_authenticated:
            # raise PermissionDenied('You must be logged in to create')
        # if serializer.is_valid():
        serializer.save()


class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()#user can see anybodys posts
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        post = self.get_object()#get_object retrieves the current instance being processed 
        # if post.author != self.request.user:
            # raise PermissionDenied('You cannot edit the post')
        serializer.save()#updates the instance with the new data from the request

    def perform_destroy(self, instance):
        # if instance.author != self.request.user:
            # raise PermissionDenied('You cant delete the post')
        instance.delete()#instance refers to the specific object that is gonna be deleted, since no new data from a serializer is required for deleting, I work derectly with the instance
        print(f'Post {instance.title} deleted successfully')