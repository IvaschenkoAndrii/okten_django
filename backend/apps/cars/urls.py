from django.urls import path

from .views import AddPhotoView, CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('',CarListView.as_view()),
    path('/<int:pk>',CarRetrieveUpdateDestroyView.as_view()),
    path('/<int:pk>/photo',AddPhotoView.as_view()),
]