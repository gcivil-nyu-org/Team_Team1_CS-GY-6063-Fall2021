from django.urls import path

from forum.views import (
    PostCreateView,
    PostDeleteView,
    PostView,
    PostListView,
    PostUpdateView,
)

app_name = "forum"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("<slug:slug>", PostView.as_view(), name="post_detail"),
    path("update/<slug:slug>", PostUpdateView.as_view(), name="post_update"),
    path("delete/<slug:slug>", PostDeleteView.as_view(), name="post_delete"),
    path("new/", PostCreateView.as_view(), name="post_create"),
]
