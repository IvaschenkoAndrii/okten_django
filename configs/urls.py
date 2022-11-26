from django.urls import path
from apps.cars.views import CarsListCreateView

urlpatterns = [
    path('cars',CarsListCreateView.as_view())
]

