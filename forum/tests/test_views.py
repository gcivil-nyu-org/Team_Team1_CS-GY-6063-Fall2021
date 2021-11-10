from django.test import RequestFactory, TestCase
from forum.forms import CommentForm
from forum.models import Post
from forum.views import PostCreateView, PostListView, PostUpdateView, PostView
from vmental.models import CustomizedUser


class CommentFormTest(TestCase):
    def test_comment_form(self):
        form_data = {"content": "test_content"}
        form = CommentForm(form_data)
        self.assertTrue(form.is_valid())


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


class PostUpdateViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = CustomizedUser.objects.create_user(username="test_user")
        self.post = Post.objects.create(
            author=self.user,
            title="test post title",
            content="test post content",
            status="draft",
        )

    def test_get_success_url(self):
        post_data = {
            "title": "updated post title",
            "content": "updated post content",
            "status": "published",
        }

        request = self.factory.post(path="forum:post_detail", data=post_data)
        request.user = self.user
        response = PostUpdateView.as_view()(request, slug=self.post.slug)

        self.assertEqual(response.status_code, 302)


class PostViewTest(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = CustomizedUser.objects.create_user(username="test_user")
        self.post = Post.objects.create(
            author=self.user,
            title="test post title",
            content="test post content",
        )

    def test_form_valid(self):
        comment_data = {
            "content": "Test post content",
        }

        request = self.factory.post(
            path="forum:post_detail", slug=self.post.slug, data=comment_data
        )
        request.user = self.user
        response = PostView.as_view()(request, slug=self.post.slug)

        self.assertEqual(response.status_code, 302)

    def test_get_context_data(self):
        request = self.factory.get("forum:post_detail", slug=self.post.slug)
        request.user = self.user
        response = PostView.as_view()(request, slug=self.post.slug)
        self.assertIsInstance(response.context_data, dict)
        self.assertEqual(len(response.context_data), 5)
