from rest_framework.serializers import ModelSerializer

from .models import CarModel, CarPhoto


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        # fields = ('id','name', 'age', 'seats', 'body_type','engine_volume')
        exclude = ('auto_park',)

class PhotoSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('photo',)