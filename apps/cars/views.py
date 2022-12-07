from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..users.permissions import IsSuperUser
from .models import CarModel, CarPhoto
from .serializers import CarSerializer, PhotoSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        query = self.request.query_params.dict()
        queryset = super().get_queryset()

        # CarModel.my_func.lt_seats(7)

        auto_park_id = query.get('name')

        if auto_park_id:
            queryset = queryset.filter(auto_park_id=auto_park_id)

        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class AddPhotoView(CreateAPIView):
    serializer_class = PhotoSerializer
    queryset = CarModel.objects.all()
    # http_method_names = ('patch',)

    def post(self, request, *args, **kwargs):
        car=self.get_object()
        data = self.request.data
        print(car)
        print(data)

        serializer = PhotoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(car=car)

        return Response(serializer.data)

    def get_permissions(self):
        if self.request.method == 'POST':
            return IsAuthenticated(),
        return IsSuperUser(),