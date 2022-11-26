from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    seats = models.IntegerField()
    body_type = models.CharField(max_length=255)
    engine_volume = models.FloatField()
