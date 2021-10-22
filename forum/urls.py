from django.urls import path

from forum.views import ForumView

urlpatterns = [
    path('', ForumView.as_view(), name='forum'),
]
