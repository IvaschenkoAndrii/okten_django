from rest_framework.serializers import ModelSerializer

from .models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        # fields = '__all__'
        # fields = ('id','name', 'age', 'seats', 'body_type','engine_volume')
        fields = ('id','name', 'age')  #*при виведені всіх машин показувати тільки (id, марку машини та рік)