from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import apps.accounts

class SignupPageTests(TestCase): # new

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, 'Sign up')
        self.assertNotContains(self.response, 
                                'Hi there! I should not be on the page.')

