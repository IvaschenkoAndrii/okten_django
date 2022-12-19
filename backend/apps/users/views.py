from typing import Type

from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from apps.auto_park.models import AutoParkModel
from apps.auto_park.serializers import AutoParkSerializer
from apps.users.models import UserModel as User

from .models import UserModel
from .permissions import IsStaff, IsSuperUser
from .serializers import AvatarSerializer, UserSerializer, UserSerializerMakeActive, UserSerializerMakeAdmin

UserModel: Type[User] = get_user_model()


class UserCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsAuthenticated,)


class UserActivationView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializerMakeActive
    permission_classes = (IsStaff,)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        user = UserModel.objects.get(pk=pk)

        serializer = UserSerializerMakeActive(user, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class UserMakeAdminView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializerMakeAdmin
    permission_classes = (IsSuperUser,)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data

        user = UserModel.objects.get(pk=pk)

        serializer = UserSerializerMakeAdmin(user, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


# class AddListAutoParkToUserView(GenericAPIView):
#     queryset = UserModel.objects.all()
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#
#         serializer = AutoParkSerializer(data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=self.request.user)
#
#         return Response(serializer.data)
#
#     def get(self, *args, **kwargs):
#         auto_park = AutoParkModel.objects.filter(user_id=self.request.user)
#         serializer = AutoParkSerializer(auto_park, many=True)
#         return Response(serializer.data)
#
#     def get_permissions(self):
#         if self.request.method == 'POST' or self.request.method == 'GET':
#             return IsAuthenticated(),
#         return IsSuperUser(),


class AutoParkListCreateView(GenericAPIView):

    def get_object(self) -> User:
        return self.request.user

    def get(self, *args, **kwargs):
        auto_parks = self.get_object().auto_parks
        serializer = AutoParkSerializer(auto_parks, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = AutoParkSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user = self.get_object()
        auto_park: AutoParkModel = serializer.save()
        auto_park.users.add(user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)


class AddAvatarView(UpdateAPIView):
    serializer_class = AvatarSerializer
    http_method_names = ('patch',)

    def get_object(self):
        return self.request.user.profile
