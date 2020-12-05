from django.forms import ModelForm

from examples.models import Location

class LocationForm(ModelForm):
    """

    Form for adding a Location object
    """
    class Meta:
        model = Location
        fields = ['name']
