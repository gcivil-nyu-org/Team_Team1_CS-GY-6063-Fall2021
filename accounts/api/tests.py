from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User


LOGIN_URL = '/api/accounts/login/'
LOGOUT_URL = '/api/accounts/logout/'
SIGNUP_URL = '/api/accounts/signup/'
LOGIN_STATUS_URL = '/api/accounts/login_status/'


class AccountApiTests(TestCase):

    def setUp(self):
        # this function will execute when each test function executes
        self.client = APIClient()
        self.user = self.createUser(
            username='admin',
            email='admin@email.com',
            password='correct password',
        )

    def createUser(self, username, email, password):
        # cannot be written as User.objects.create() as password needs to be
        # encrypted, username and email needs normalization
        return User.objects.create_user(username, email, password)

    def test_login(self):
        # test functions must start with test_ to be called automatically
        # must use post rather than get
        response = self.client.get(LOGIN_URL, {
            'username': self.user.username,
            'password': 'correct password',
        })
        # login failed，http status code returns 405 = METHOD_NOT_ALLOWED
        self.assertEqual(response.status_code, 405)

        # use post with incorrect password
        response = self.client.post(LOGIN_URL, {
            'username': self.user.username,
            'password': 'wrong password',
        })
        self.assertEqual(response.status_code, 400)

        # verifying without logging in
        response = self.client.get(LOGIN_STATUS_URL)
        self.assertEqual(response.data['has_logged_in'], False)
        # use correct password
        response = self.client.post(LOGIN_URL, {
            'username': self.user.username,
            'password': 'correct password',
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data['user'], None)
        self.assertEqual(response.data['user']['email'], 'admin@email.com')
        # verifying after logged in
        response = self.client.get(LOGIN_STATUS_URL)
        self.assertEqual(response.data['has_logged_in'], True)

    def test_logout(self):
        # login first
        self.client.post(LOGIN_URL, {
            'username': self.user.username,
            'password': 'correct password',
        })
        # verify that user has logged in
        response = self.client.get(LOGIN_STATUS_URL)
        self.assertEqual(response.data['has_logged_in'], True)

        # must use post for the test
        response = self.client.get(LOGOUT_URL)
        self.assertEqual(response.status_code, 405)

        # switch to post and successfully logout
        response = self.client.post(LOGOUT_URL)
        self.assertEqual(response.status_code, 200)
        # verify that the user has logged out
        response = self.client.get(LOGIN_STATUS_URL)
        self.assertEqual(response.data['has_logged_in'], False)

    def test_signup(self):
        data = {
            'username': 'someone',
            'email': 'someone@email.com',
            'password': 'any password',
        }
        # test with get request
        response = self.client.get(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 405)

        # test with incorrect email
        response = self.client.post(SIGNUP_URL, {
            'username': 'someone',
            'email': 'not a correct email',
            'password': 'any password'
        })
        # print(response.data)
        self.assertEqual(response.status_code, 400)

        # testing with password too short
        response = self.client.post(SIGNUP_URL, {
            'username': 'someone',
            'email': 'someone@email.com',
            'password': '123',
        })
        # print(response.data)
        self.assertEqual(response.status_code, 400)

        # testing with long user name
        response = self.client.post(SIGNUP_URL, {
            'username': 'username is tooooooooooooooooo loooooooong',
            'email': 'someone@email.com',
            'password': 'any password',
        })
        # print(response.data)
        self.assertEqual(response.status_code, 400)

        # successfully registered
        response = self.client.post(SIGNUP_URL, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['user']['username'], 'someone')
        # verify that the user has logged in
        response = self.client.get(LOGIN_STATUS_URL)
        self.assertEqual(response.data['has_logged_in'], True)
