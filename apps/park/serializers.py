from rest_framework.serializers import ModelSerializer

from models import AutoParkModel


class AutoParkSerializer:
    class Meta:
        model = AutoParkModel
        fields = '__all__'
