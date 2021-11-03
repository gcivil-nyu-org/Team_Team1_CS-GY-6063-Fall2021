from vmental.models import CustomizedUser
from django.test import TestCase
from forum.models import Post, Comment
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

    def test_get_comments_count(self):
        test_user = CustomizedUser.objects.create_user(username="teset_user")
        post = Post.objects.create(
            author=test_user,
            title="test_title",
            content="test_content",
        )
        post.save()
        comment_1 = Comment.objects.create(
            post=post, author=test_user, content="Test comment 1 by test_user"
        )
        comment_1.save()
        comment_2 = Comment.objects.create(
            post=post, author=test_user, content="Test comment 2 by test_user"
        )
        comment_2.save()
        comment_3 = Comment.objects.create(
            post=post, author=test_user, content="Test comment 3 by test_user"
        )
        comment_3.save()
        self.assertEqual(3, post.get_comments_count())

    def test_get_absolute_url(self):
        test_user = CustomizedUser.objects.create_user(username="test_user")
        self.post = Post.objects.create(
            author=test_user,
            title="Hello, world!",
            content="This is the content of a sample post.",
        )
        self.assertEqual("/forum/hello-world", self.post.get_absolute_url())


class CommentModelTests(TestCase):
    def test_hours_to_now(self):
        test_user = CustomizedUser.objects.create_user(username="test_user")
        post = Post.objects.create(
            author=test_user,
            title="Hello, world!",
            content="This is the content of a sample post.",
        )
        post.save()
        comment = Comment.objects.create(
            post=post, author=test_user, content="Test comment by test_user"
        )
        comment.created_at = utc_now() - timedelta(hours=10)
        comment.save()
        self.assertEqual(comment.hours_to_now, 10)

    def test__str__(self):
        test_user = CustomizedUser.objects.create_user(username="test_user")
        post = Post.objects.create(
            author=test_user,
            title="Hello, world!",
            content="This is the content of a sample post.",
        )
        post.save()
        comment = Comment.objects.create(
            post=post, author=test_user, content="Test comment by test_user"
        )
        comment.save()
        self.assertEqual("1 test_user: 1 \n Test comment by test_user", str(comment))
