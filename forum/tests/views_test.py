from vmental.models import CustomizedUser
from django.test import TestCase, RequestFactory
from forum.models import Post
from forum.views import PostListView
from forum.forms import CommentForm


class PostListViewTests(TestCase):
    def test_get_queryset(self):
        test_user = CustomizedUser.objects.create_user(username="test_user")
        post_1 = Post.objects.create(
            author=test_user,
            title="test_title_1",
            content="test_content_1",
        )
        post_1.save()
        post_2 = Post.objects.create(
            author=test_user,
            title="test_title_2",
            content="test_content_2",
        )
        post_2.save()
        post_3 = Post.objects.create(
            author=test_user,
            title="test_title_3",
            content="test_content_3",
        )
        post_3.save()
        request = RequestFactory().get("/forum/")
        view = PostListView()
        view.request = request
        qs = view.get_queryset()
        self.assertQuerysetEqual(qs, Post.objects.all().order_by("-created_at"))


class CommentFormTest(TestCase):
    def test_comment_form(self):
        form_data = {"content": "test_content"}
        form = CommentForm(form_data)
        self.assertTrue(form.is_valid())