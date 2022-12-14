from django.core import validators as V
from django.db import models

from apps.auto_park.models import AutoParkModel

from .managers import CarManager
from .services import upload_photo


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    name = models.CharField(max_length=20, unique=True, validators=[
        V.MinLengthValidator(2), V.MaxLengthValidator(20)
    ])
    price = models.FloatField(max_length=9)
    age = models.IntegerField(default=10)
    seats = models.IntegerField()
    body_type = models.CharField(max_length=20, blank=True)
    engine_volume = models.FloatField()
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # objects=CarManager()
    # objects = models.Manager()
    # my_func=CarManager()


class CarPhoto(models.Model):
    class Meta:
        db_table = 'cars_photo'

    photo = models.ImageField(upload_to=upload_photo)
    car = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='photo')
