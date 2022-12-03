from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import UserModel
from .permissions import IsStaff, IsSuperUser
from .serializers import UserSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (IsSuperUser,)


class UserActivationView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserModel.objects.all()
    permission_classes = (AllowAny,)

    def patch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.data)
        return Response(serializer.data)

    # def post(self, request, *args, **kwargs):
    #     pk = kwargs.get('pk')
    #     data=self.request.data
    #     user = UserModel.objects.filter(id=pk)
    #     serializer = UserSerializer(user)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save(user=user)
    #     print(serializer.data)
    #     return Response(serializer.data)
