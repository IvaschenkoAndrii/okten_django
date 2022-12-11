from typing import Type

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.auth.serializers import EmailSerializer, PasswordSerializer
from apps.users.models import UserModel as User

from core.services.email_service import EmailService
from core.services.jwt_service import ActivateToken, JWTService, RecoveryToken

UserModel: Type[User] = get_user_model()


class ActivateUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def get(self, *args, **kwargs):
        token = kwargs.get('token')
        user = JWTService.validate_token(token, ActivateToken)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)


class RecoveryUserView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        email = self.request.data

        serializer = EmailSerializer(data=email)
        serializer.is_valid(raise_exception=True)

        email = serializer.data['email']
        user = UserModel.objects.get(email=email)

        EmailService.recovery_by_email(user)

        return Response(status=status.HTTP_200_OK)


class ChangeUserPasswordView(GenericAPIView):
    permission_classes = (AllowAny,)

    def post(self, *args, **kwargs):
        token = self.kwargs.get('token')
        user = JWTService.validate_token(token, RecoveryToken)
        data = self.request.data

        serializer = PasswordSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        password = serializer.data['password']

        user.set_password(password)
        user.save()
        return Response(status=status.HTTP_200_OK)
