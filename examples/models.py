from django.db import models



class Location(models.Model):
    """

    User entered location.
    """
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class TravelData(models.Model):
    """

    Captures anonymous data about miles travelled and mode of transport
    in different areas of the world.
    """
    modes_of_transport = (
        (0, 'Automobile'),
        (1, 'Bicycle'),
        (2, 'Walking'),
        (3, 'Train'),
        (4, 'Subway'),
        (5, 'Other'))

    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT)
    mode_of_transport = models.IntegerField(choices=modes_of_transport)
    miles_travelled = models.FloatField()

    class Meta:
        ordering = ['-created_at']
