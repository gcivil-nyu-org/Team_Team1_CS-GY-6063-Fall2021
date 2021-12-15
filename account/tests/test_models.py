from account.models import CustomizedUser
from django.test import TestCase
from django.urls import reverse


class VMMentalHealthTest(TestCase):
    def test_html_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def createUser(self, username, email, password):
        return CustomizedUser.objects.create(username="test_user1", password="test1234")

    def test_html_login_page(self):
        response = self.client.get("/auth/login/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            "/auth/login/",
            {"username": "abcd", "password": "abc123def456"},
        )
        self.assertEqual(response.status_code, 200)

    def test_html_login_page_failtest(self):
        response = self.client.get("/auth/login/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post(
            "/auth/login/",
            {"username": "test_user2", "password": "test12341231"},
        )
        self.assertIn(
            "Please enter a correct username and password.", str(response.content)
        )

    def test_html_signup_page(self):
        response = self.client.post(
            reverse("signup"),
            {
                "email": "abc@test.com",
                "username": "test8901",
                "first_name": "test",
                "last_name": "test1234",
                "gender": "F",
                "date_of_birth": "03/17/1998",
                "phone_number": "1234567890",
                "password1": "Passw0rd!",
                "password2": "Passw0rd!",
            },
        )
        self.assertEqual(response.status_code, 200)
