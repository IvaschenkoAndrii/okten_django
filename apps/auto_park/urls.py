from django.urls import path

from .views import AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView, ListCreateAutoParkView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', ListCreateAutoParkView.as_view()),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view())
]
