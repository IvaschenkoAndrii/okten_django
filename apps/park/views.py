from rest_framework.generics import ListCreateAPIView

from models import AutoParkModel
from serializers import AutoParkSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer
