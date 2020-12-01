from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from examples.models import (
    Location,
    TravelData)


class Index(TemplateView):
    """

    Landing page for the examples app.
    """
    template_name = 'examples/index.html'


class TravelDataList(ListView):
    """

    List of all travel data.
    """
    model = TravelData
    paginate_by = 50


class CreateTravelData(CreateView):
    """

    Create a new travel data entry.
    """
    model = TravelData
    fields = [
    'location',
    'mode_of_transport',
    'miles_travelled']
    success_url = reverse_lazy('examples:index')
