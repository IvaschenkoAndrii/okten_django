from django.db import models

from apps.users.models import UserModel


class AutoParkModel(models.Model):
    class Meta:
        db_table = 'auto_park'

    name = models.CharField(max_length=20)
    users = models.ManyToManyField(UserModel, through='UsersAutoParksModel', related_name='auto_parks')


class UsersAutoParksModel(models.Model):
    class Meta:
        db_table = 'cars_auto_parks'

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    auto_park = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE)