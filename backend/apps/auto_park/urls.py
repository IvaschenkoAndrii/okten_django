from django.urls import path

from .views import AutoParkListCreateView, AutoParkRetrieveUpdateDestroyView, CarListCreateAutoParkView

urlpatterns = [
    path('', AutoParkListCreateView.as_view()),
    path('/<int:pk>/cars', CarListCreateAutoParkView.as_view()),
    path('/<int:pk>', AutoParkRetrieveUpdateDestroyView.as_view())
]
