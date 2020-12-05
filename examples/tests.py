from django.test import TestCase
from django.test import Client
from django.urls import reverse

from examples.models import (
    Location,
    TravelData)


class TestURLS(TestCase):
    """

    Test that all urls return without errors.
    """

    def setUp(self):
        self.client = Client()


    def test_index(self):
        url = reverse('examples:index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_get_traveldata_form(self):
        url = reverse('examples:create-traveldata')
        response = self.client.get(url)
        self.assertContains(response, "<form")


    def test_post_traveldata(self):
        location = Location.objects.create(name='Tokyo, Japan')
        data = {
            'location': location.pk,
            'mode_of_transport': 1,
            'miles_travelled': 10.49
        }
        url = reverse('examples:create-traveldata')
        response = self.client.post(url, data=data)
        self.assertEquals(response.status_code, 302)


    def test_traveldata_list(self):
        location = Location.objects.create(name='Los Angeles')
        travel_data = TravelData.objects.create(
            location=location,
            mode_of_transport=0,
            miles_travelled=47)
        url = reverse('examples:traveldata-list')
        response = self.client.get(url)
        self.assertContains(response, 'Los Angeles')


    def test_post_location(self):
        data = {
            'name': "London, UK"
        }
        url = reverse('examples:create-location')
        response = self.client.post(url, data=data)
        self.assertEquals(response.status_code, 302)
