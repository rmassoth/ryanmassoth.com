from django.urls import path

from blog.views import (
    Index,
    PostDetail)

app_name = "blog"
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('<str:slug>/', PostDetail.as_view(), name='post-detail')
]