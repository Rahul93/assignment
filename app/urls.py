from django.urls import path
from app.views import LocationListCreateView, LocationDetailView

urlpatterns = [
    # List all locations or create a new location
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),

    # Retrieve, update, or delete a specific location by `uuid`
    path('locations/<uuid:uuid>/', LocationDetailView.as_view(), name='location-detail'),
]