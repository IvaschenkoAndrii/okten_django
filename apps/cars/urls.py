from django.urls import path

from .views import CarRetrieveUpdateDestroyView, CarListView

urlpatterns = [
    path('',CarListView.as_view()),
    path('/<int:pk>',CarRetrieveUpdateDestroyView.as_view())
]