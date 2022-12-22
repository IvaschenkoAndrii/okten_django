# Generated by Django 4.1.3 on 2022-12-07 15:27

from django.db import migrations, models

import apps.cars.services


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_remove_carphoto_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carphoto',
            name='photo1',
        ),
        migrations.AddField(
            model_name='carphoto',
            name='photo',
            field=models.ImageField(blank=True, upload_to=apps.cars.services.upload_photo),
        ),
    ]