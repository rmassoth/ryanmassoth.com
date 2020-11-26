from django.db import models


class Post(models.Model):
    """

    Blog posts for ryanmassoth.com
    """
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog.views.detail', args=[self.slug])

    class Meta:
        verbose_name_plural = "posts"
        ordering = ('-created_at',)
