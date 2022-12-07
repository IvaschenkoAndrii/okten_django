from django.urls import path

from .views import AddAvatarView, AddListAutoParkToUserView, UserActivationView, UserCreateView, UserMakeAdminView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>/active', UserActivationView.as_view()),
    path('/<int:pk>/admin', UserMakeAdminView.as_view()),
    path('/<int:pk>/auto_park', AddListAutoParkToUserView.as_view()),
    path('/auto_parks', AddListAutoParkToUserView.as_view()),
    path('/avatar', AddAvatarView.as_view()),
]
