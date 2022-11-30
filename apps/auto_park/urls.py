from django.urls import path

from views import AutoParkListCreateView

urlpatterns = [
    path('', AutoParkListCreateView.as_view())
]
