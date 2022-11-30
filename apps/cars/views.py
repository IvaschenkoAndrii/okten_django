from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from .serializers import CarSerializer
from .models import CarModel


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get(self, *args, **kwargs):
        query = self.request.query_params.dict()
        print('query')

        queryset = super().get_queryset()

        auto_park_id = query.get('auto_park_id')
        print(auto_park_id)

        if auto_park_id:
            queryset = queryset.filter(id=auto_park_id)

        return queryset


