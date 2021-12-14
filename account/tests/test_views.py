from django.test import TestCase, RequestFactory
from django.urls import reverse
from account.models import CustomizedUser
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from account.tokens import account_activation_token
from account.views import SignUp


class test_signup_view(TestCase):
    def setUp(self) -> None:
        self.factory = RequestFactory()
        self.user = CustomizedUser.objects.create(
            username="test_user1", password="test1234", date_of_birth="1994-10-10"
        )

    def test_get(self):
        request = self.factory.get(path="signup.html")
        response = SignUp.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        post_data = {
            "username": "test123",
            "email": "test123@test.com",
            "first_name": "test",
            "last_name": "123",
            "gender": "M",
            "date_of_birth": "1996-07-07",
            "phone_number": "9876543321",
            "password": "abc123def456",
            "password2": "abc123def456",
        }
        request = self.factory.post(path="signup.html", data=post_data)
        response = SignUp.as_view()(request)
        print(response.content)
        self.assertEqual(response.status_code, 200)


class test_email_functions(TestCase):
    def create_user(self):
        return CustomizedUser.objects.create(
            username="test_user1", password="test1234", date_of_birth="1994-10-10"
        )

    def test_valid_verification(self):
        temp_user = self.create_user()
        uid64 = urlsafe_base64_encode(force_bytes(temp_user.pk))
        token = account_activation_token.make_token(temp_user)
        url = reverse("activate", args=[uid64, token])
        response = self.client.get(url)
        self.assertNotIn("Activation link is invalid!", str(response.content))
        self.assertEqual(response.status_code, 200)

    def test_invalid_verification(self):
        temp_user = self.create_user()
        uid64 = urlsafe_base64_encode(force_bytes(100000))
        token = account_activation_token.make_token(temp_user)
        url = reverse("activate", args=[uid64, token])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn("Activation link is invalid!", str(response.content))
