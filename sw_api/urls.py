from django.urls import path

from sw_api.views.planets_view import PlanetsView
from sw_api.views.planet_details_view import PlanetDetailsView


urlpatterns = [
    path('planets', PlanetsView.as_view(), name='planets'),
    path('planets/<int:planet_id>', PlanetDetailsView.as_view(), name='planet_details'),
]
