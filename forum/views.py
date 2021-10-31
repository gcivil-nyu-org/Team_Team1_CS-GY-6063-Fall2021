from django.views.generic import ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from forum.models import Comment, Post


@method_decorator(login_required, name="dispatch")
class PostListView(ListView):
    model = Post
    template_name = "post_list"

    def get_queryset(self):
        return Post.objects.all().order_by("-created_at")


@method_decorator(login_required, name="dispatch")
class PostDetailView(DetailView):
    model = Post


@method_decorator(login_required, name="dispatch")
class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "content"]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={
                "pk": self.object.pk,
            },
        )


@method_decorator(login_required, name="dispatch")
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content"]

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


@method_decorator(login_required, name="dispatch")
class CommentCreateView(CreateView):
    model = Comment
    fields = ["content"]
    success_url = reverse_lazy("post_list")

    def get_success_url(self):
        return reverse_lazy(
            "post_detail",
            kwargs={
                "pk": self.request.GET.get("post_id"),
            },
        )

    def form_valid(self, form):
        post = Post.objects.get(id=self.request.GET.get("post_id"))
        author = self.request.user
        form.instance.author = author
        form.instance.post = post
        return super(CommentCreateView, self).form_valid(form)
