
from .views import PostListCreateView, PostRetrieveUpdateDestroyView
from django.urls import path

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail')


]