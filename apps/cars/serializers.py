import os

from django.db import transaction

from rest_framework.serializers import ModelSerializer

from .models import CarModel, CarPhoto


class PhotoSerializer(ModelSerializer):
    class Meta:
        model = CarPhoto
        fields = ('photo',)

    def to_representation(self, instance: CarPhoto):
        return instance.photo.url


class CarSerializer(ModelSerializer):
    photo = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = CarModel
        exclude = ('auto_park',)
