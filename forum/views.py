from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView, UpdateView
from django.views.generic.edit import CreateView, DeleteView, FormMixin

from forum.forms import CommentForm
from forum.models import Post


@method_decorator(login_required, name="dispatch")
class PostListView(ListView):
    model = Post
    template_name = "forum:post_list"

    def get_queryset(self):
        published_qs = Post.objects.filter(status="published")
        curr_user_qs = Post.objects.filter(author=self.request.user.id)
        return published_qs.union(curr_user_qs).order_by("-created_at")


@method_decorator(login_required, name="dispatch")
class PostView(FormMixin, DetailView):
    model = Post
    temmplate_name = "forum:test"
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy("forum:post_detail", kwargs={"slug": self.object.slug},)

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context["form"] = CommentForm(initial={"post": self.get_object})
        context["comments"] = self.object.comments.all()
        return context

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        form.instance.post = self.object
        return super(PostView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = self.request.user
            comment.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@method_decorator(login_required, name="dispatch")
class PostUpdateView(UpdateView):
    model = Post
    fields = [
        "title",
        "content",
        "status",
    ]
    template_name_suffix = "_update"

    def get_success_url(self):
        return reverse_lazy("forum:post_detail", kwargs={"slug": self.object.slug,},)


@method_decorator(login_required, name="dispatch")
class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("forum:post_list")


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    fields = [
        "title",
        "content",
        "status",
    ]

    def get_success_url(self):
        return reverse_lazy("forum:post_detail", kwargs={"slug": self.object.slug},)

    def form_valid(self, form):
        author = self.request.user
        form.instance.author = author
        return super(PostCreateView, self).form_valid(form)
