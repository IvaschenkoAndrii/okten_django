from django.urls import path

from .views import AddListAutoParkToUserView, UserActivationView, UserCreateView, UserMakeAdminView

urlpatterns = [
    path('', UserCreateView.as_view()),
    path('/<int:pk>/active', UserActivationView.as_view()),
    path('/<int:pk>/admin', UserMakeAdminView.as_view()),
    path('/<int:pk>/auto_park', AddListAutoParkToUserView.as_view()),
]
