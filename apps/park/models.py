from django.db import models


class parkModel(models.Model):
    class Meta:
        db_table = 'park'

    name = 'park'
