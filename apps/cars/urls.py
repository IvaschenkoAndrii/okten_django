from django.urls import path

from .views import CarsListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('',CarsListCreateView.as_view()),
    path('/<int:pk>',CarRetrieveUpdateDestroyView.as_view())
]