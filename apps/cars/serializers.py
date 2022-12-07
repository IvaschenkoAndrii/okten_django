from django.db import transaction

from rest_framework.serializers import ModelSerializer

from .models import CarModel, CarPhoto


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = CarPhoto
        # fields='__all__'
        fields = ('photo',)


class CarSerializer(ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        exclude = ('auto_park',)
