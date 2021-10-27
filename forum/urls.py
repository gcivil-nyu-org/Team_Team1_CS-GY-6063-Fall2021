from django.urls import path

from forum.views import (
    PostCreateView,
    PostDeleteView,
    PostDetailView,
    PostListView,
    PostUpdateView,
    CommentCreateView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<int:pk>", PostDetailView.as_view(), name="post_detail"),
    path("update/<int:pk>", PostUpdateView.as_view(), name="post_update"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="post_delete"),
    path("new/", PostCreateView.as_view(), name="post_create"),
    path("comment/", CommentCreateView.as_view(), name="comment_create"),
]
