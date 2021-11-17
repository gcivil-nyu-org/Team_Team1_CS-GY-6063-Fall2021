from django.test import TestCase
from django.urls import reverse
from account.models import CustomizedUser
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from account.tokens import account_activation_token

# from django.core import mail
#
# from vmental.views import signup


# class test_email_functions(TestCase):
#     def create_user(self):
#         return CustomizedUser.objects.create(username="test_user1", password="test1234")

#     def test_valid_verification(self):
#         temp_user = self.create_user()
#         uid64 = urlsafe_base64_encode(force_bytes(temp_user.pk))
#         token = account_activation_token.make_token(temp_user)
#         url = reverse("activate", args=[uid64, token])
#         response = self.client.post(url)
#         self.assertNotIn("Activation link is invalid!", str(response.content))
#         self.assertEqual(response.status_code, 200)

#     def test_invalid_verification(self):
#         temp_user = self.create_user()
#         uid64 = urlsafe_base64_encode(force_bytes(100000))
#         token = account_activation_token.make_token(temp_user)
#         url = reverse("activate", args=[uid64, token])
#         response = self.client.post(url)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn("Activation link is invalid!", str(response.content))
