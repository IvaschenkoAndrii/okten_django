from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer


class CarsListCreateView(APIView):

    def get(self, *args, **kwargs):
        users = CarModel.objects.all()
        serializer = CarSerializer(instance=users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
