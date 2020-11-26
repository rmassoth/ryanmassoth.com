from django.urls import path

from home.views import (
    Index,
    AboutSite,
    AboutMe)

app_name = "home"
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about-site/', AboutSite.as_view(), name='about-site'),
    path('about-me/', AboutMe.as_view(), name='about-me')
]