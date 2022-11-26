from django.urls import path
from apps.cars.views import CarsListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('cars',CarsListCreateView.as_view()),
    path('cars/<int:pk>',CarRetrieveUpdateDestroyView.as_view())
]

