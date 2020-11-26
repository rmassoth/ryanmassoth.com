from django.test import TestCase
from django.test import Client
from django.urls import reverse


class TestURLS(TestCase):
    """

    Test that all urls return without errors.
    """

    def setUp(self):
        self.client = Client()


    def test_index(self):
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
