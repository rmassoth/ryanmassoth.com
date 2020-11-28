from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from blog.models import Post


class Index(ListView):
    """

    The main page for viewing blogs. This will default to a 
    list of most recent posts and be paginated.
    """
    model = Post
    paginate_by = 30
    template_name = 'blog/index.html'
    queryset = Post.objects.filter(published=True).order_by("-created_at")


class PostDetail(DetailView):
    """

    Returns the full blog post on a single page.
    """
    model = Post
