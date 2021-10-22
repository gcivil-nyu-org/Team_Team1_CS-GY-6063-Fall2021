from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from forum.models import Post


class ForumView(ListView, LoginRequiredMixin):
    model = Post
    login_url = 'login'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')


class PostDetailView(DetailView):
    model = Post
