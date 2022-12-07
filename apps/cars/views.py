from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView

from .models import CarModel
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


class AddPhotoView(UpdateAPIView):
    serializer_class = PhotoSerializer
    queryset = CarModel.objects.all()
    http_method_names = ('patch',)
