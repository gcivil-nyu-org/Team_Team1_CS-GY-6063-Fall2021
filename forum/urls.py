from django.urls import path

from forum.views import PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail'),
]
