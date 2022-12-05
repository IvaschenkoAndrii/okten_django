import status as status

from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import UserModel
from .permissions import IsStaff, IsSuperUser
from .serializers import UserSerializer, UserSerializerMakeActive, UserSerializerMakeAdmin


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    # queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)


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
