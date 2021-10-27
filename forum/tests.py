from vmental.models import CustomizedUser
from django.test import TestCase
from forum.models import Post
from datetime import timedelta
from utils.time_helpers import utc_now


class PostTests(TestCase):
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
