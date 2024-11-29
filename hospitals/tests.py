from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.login_url = reverse('login')  # Ensure this matches your login view name

    def test_login_page_loads(self):
        # Test if the login page loads correctly
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Login")  # Assumes "Login" text appears on the page

    def test_login_successful(self):
        # Test successful login
        response = self.client.post(self.login_url, {'uname': 'testuser', 'pwd': 'testpassword'})
        self.assertRedirects(response, reverse('index'))  # Adjust the redirect URL as per your app
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_invalid_credentials(self):
        # Test login with invalid credentials
        response = self.client.post(self.login_url, {'uname': 'wronguser', 'pwd': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Invalid")  # Assumes "Invalid" or similar message appears
        self.assertFalse(response.wsgi_request.user.is_authenticated)
