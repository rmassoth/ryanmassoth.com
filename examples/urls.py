from django.urls import path

from examples.views import (
    Index,
    TravelDataList,
    CreateTravelData,
    CreateLocation)

app_name = "examples"
urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('traveldata/create/',
         CreateTravelData.as_view(),
         name='create-traveldata'),
    path('traveldata/', TravelDataList.as_view(), name='traveldata-list'),
    path('locations/create/', CreateLocation.as_view(), name='create-location')
]