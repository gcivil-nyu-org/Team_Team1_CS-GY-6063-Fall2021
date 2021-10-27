from vmental.models import CustomizedUser
from django.test import TestCase, RequestFactory
from forum.models import Post
from forum.views import PostListView
from forum.forms import CommentForm
from datetime import timedelta
from utils.time_helpers import utc_now


class PostModelTests(TestCase):
    def test_hours_to_now(self):
        test_user = CustomizedUser.objects.create_user(username="test_user")
        post = Post.objects.create(
            author=test_user,
            title="Hello, world!",
            content="This is the content of a sample post.",
        )
        post.created_at = utc_now() - timedelta(hours=10)
        post.save()
        self.assertEqual(post.hours_to_now, 10)

    def test__str__(self):
        test_user = CustomizedUser.objects.create_user(username="teset_user")
        post = Post.objects.create(
            author=test_user,
            title="test_title",
            content="test_content",
        )
        post.save()
        self.assertEqual("1 teset_user: test_title \n test_content", str(post))


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
