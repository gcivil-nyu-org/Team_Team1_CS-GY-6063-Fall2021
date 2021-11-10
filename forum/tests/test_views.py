from vmental.models import CustomizedUser
from django.test import TestCase, RequestFactory, Client
from forum.models import Post
from forum.views import PostCreateView, PostListView
from forum.forms import CommentForm
from django.urls import reverse
from django.utils.text import slugify


class PostCreateViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = CustomizedUser.objects.create_user(username="test_user")

    def test_form_valid(self):
        post_data = {
            "title": "Test post title",
            "content": "Test post content",
            "status": "draft",
        }

        request = self.factory.post(path="forum:post_create", data=post_data)
        request.user = self.user
        response = PostCreateView.as_view()(request)

        self.assertEqual(response.status_code, 302)


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
        request.user = test_user
        view = PostListView()
        view.request = request
        qs = view.get_queryset()
        self.assertQuerysetEqual(qs, Post.objects.all().order_by("-created_at"))


class PostUpdateViewTests(TestCase):
    def test_get_queryset(self):
        self.client = Client()
        test_user = CustomizedUser.objects.create_user(
            username="test_user_2", email="test_user_2@test_user.com"
        )
        test_user.set_password("abc123def456")
        test_user.save()
        self.client.login(username=test_user.username, password="abc123def456")
        # self.client.force_login(user=test_user)
        post_1 = Post.objects.create(
            author=test_user,
            title="test_title_1",
            # content="test_content_1",
        )
        post_1.save()
        # print()
        response = self.client.post(
            reverse("forum:post_update", kwargs={"slug": slugify(post_1.title)}),
            {
                "title": "test_title_2",
                "content": "test_content_2",
                "status": "published",
            },
        )
        self.assertEqual(response.status_code, 302)
        post_1.refresh_from_db()
        self.assertEqual(post_1.title, "test_title_2")


class CommentFormTest(TestCase):
    def test_comment_form(self):
        form_data = {"content": "test_content"}
        form = CommentForm(form_data)
        self.assertTrue(form.is_valid())
