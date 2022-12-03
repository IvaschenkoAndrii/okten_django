from django.urls import path

from .views import UserActivationView, UserCreateView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>', UserActivationView.as_view())
]
