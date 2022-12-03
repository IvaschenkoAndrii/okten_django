from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import CarModel
from .serializers import CarSerializer


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
