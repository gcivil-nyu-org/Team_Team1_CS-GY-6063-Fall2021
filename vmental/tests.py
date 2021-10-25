from django.test import TestCase, client
import datetime
from django.utils import timezone
from django.urls import reverse
from vmental.models import *
from vmental.views import *


# Create your tests here.

class VMMentalHealthTest(TestCase):
    def test_html_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def createUser(self, username, email, password):
        # cannot be written as User.objects.create() as password needs to be
        # encrypted, username and email needs normalization
        return CustomizedUser.objects.create(username='test_user1', password='test1234')

    def test_html_login_page(self):
        response = self.client.get("/auth/login/")
        self.assertEqual(response.status_code, 200)

        CustomizedUser.objects.create(username='test_user1', password='test1234', date_of_birth='1997-10-09',
                                      is_provider=False)
        response = self.client.post("/auth/login/", {'username': "test_user1", 'password': "test1234"}, )
        self.assertEqual(response.status_code, 200)

    def test_html_login_page_failtest(self):
        response = self.client.get("/auth/login/")
        self.assertEqual(response.status_code, 200)

        response = self.client.post("/auth/login/", {'username': "test_user2", 'password': "test12341231"}, )
        self.assertIn("Please enter a correct username and password.", str(response.content))

    def test_html_signup_failtest(self):
        response_wrong_email = self.client.post("/auth/signup",
                                                {'email': 'test', 'username': 'test123', 'first_name': 'test',
                                                 'last_name': 'test1234', 'gender': 'F', 'date_of_birth': '03/17/1998',
                                                 'phone_number': 123123123, 'password1': 'test123abc456',
                                                 'password2': 'test123abc456'})
        print(response_wrong_email)
        print(response_wrong_email.content)

    def test_html_signup_page(self):
        response = self.client.post("/auth/signup",
                                    {'email': 'test@test.com', 'username': 'test8901', 'first_name': 'test',
                                     'last_name': 'test1234', 'gender': 'F', 'date_of_birth': '03/17/1998',
                                     'phone_number': 123123123, 'password1': 'test123abc456',
                                     'password2': 'test123abc456'}, enforce_csrf_checks=True)
        print(response)
        print(response.content)
        self.assertEqual(response.status_code, 301)

        response1 = self.client.post("/auth/login/", {'username': "test8901", 'password': "test123abc456"}, )
        # print(response1)
        # print(response1.content)
        # self.assertEqual(response.status_code, 200)
        self.assertNotIn("Please enter a correct username and password.", str(response1.content))