from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from .views import ActivateUserView, ChangeUserPasswordView, RecoveryUserView

urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('/refresh', TokenRefreshView.as_view()),
    path('/activate/<str:token>', ActivateUserView.as_view()),
    path('/password/<str:token>', ChangeUserPasswordView.as_view()),
    path('/recovery', RecoveryUserView.as_view()),
]
