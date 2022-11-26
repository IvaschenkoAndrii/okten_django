from rest_framework.serializers import ModelSerializer

from apps.cars.models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        # fields = ('name', 'age', 'seats', 'body_type','engine_volume')