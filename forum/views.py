from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers
from forum.models import Comment, Post
from forum.forms import CommentForm


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    login_url = "login"

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    login_url = "login"


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name_suffix = "_update"


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")
    login_url = "login"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "content"]
    login_url = "login"

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={
                "pk": self.object.pk,
            },
        )

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super(PostCreateView, self).form_valid(form)


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ["content"]
    login_url = "login"
    success_url = reverse_lazy("post_list")

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={
                "pk": self.request.GET.get('post_id'),
            },
        )

    def form_valid(self, form):
        post = Post.objects.get(id=self.request.GET.get('post_id'))
        author = self.request.user
        form.instance.author = author
        form.instance.post = post
        return super(CommentCreateView, self).form_valid(form)
