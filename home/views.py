from django.shortcuts import render
from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = 'home/index.html'


class AboutSite(TemplateView):
    template_name = 'home/about_site.html'


class AboutMe(TemplateView):
    template_name = 'home/about_me.html'
