from django.urls import path

from forum.views import ForumView, PostDetailView

urlpatterns = [
    path('', ForumView.as_view(), name='post_list'),
    path('<int:pk>', PostDetailView.as_view(), name='post_detail')
]
