from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            Response(serializer.errors)

        car = CarModel.objects.create(**serializer.data)

        serializer = CarSerializer(instance=car)
        return Response(serializer.data)
