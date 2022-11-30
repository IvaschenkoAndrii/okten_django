from django.urls import path

from .views import AutoParkListCreateView, AddCarToAutoParkView, AutoParkRetrieveUpdateDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', AddCarToAutoParkView.as_view()),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view())
]
