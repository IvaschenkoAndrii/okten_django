from django.urls import path

from .views import AddAvatarView, AutoParkListCreateView, UserActivationView, UserCreateView, UserMakeAdminView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>/active', UserActivationView.as_view()),
    path('/<int:pk>/admin', UserMakeAdminView.as_view()),
    path('/<int:pk>/auto_park', AutoParkListCreateView.as_view()),
    path('/auto_parks', AutoParkListCreateView.as_view()),
    path('/avatar', AddAvatarView.as_view()),
]
