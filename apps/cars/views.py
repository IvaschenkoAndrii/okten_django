from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView

from .serializers import CarSerializer
from .models import CarModel



class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        query = self.request.query_params.dict()
        queryset = super().get_queryset()
        auto_park_id = query.get('name')

        if auto_park_id:
            queryset = queryset.filter(auto_park_id=auto_park_id)

        return queryset


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
