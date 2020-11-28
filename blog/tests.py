from django.test import TestCase
from django.test import Client
from django.urls import reverse

from blog.models import Post


class TestURLS(TestCase):
    """

    Test that all urls return without errors.
    """

    def setUp(self):
        self.client = Client()


    def test_index(self):
        published_post = Post.objects.create(
            title="This is a title",
            slug="this-is-a-title",
            body="Here is some text.",
            published=True)
        unpublished_post = Post.objects.create(
            title="Never gonna post this",
            slug="never-gonna-post-this",
            body="This is a dummy post.",
            published=False)
        url = reverse('blog:index')
        response = self.client.get(url)
        self.assertContains(response, "This Is A Title")
        self.assertNotContains(response, "Never Gonna Post This")


    def test_get_post(self):
        post = Post.objects.create(
            title="This is a title",
            slug="this-is-a-title",
            body="Here is some text.",
            published=True)
        url = reverse('blog:post-detail', kwargs={"slug": post.slug})
        response = self.client.get(url)
        self.assertContains(response, "This Is A Title")
