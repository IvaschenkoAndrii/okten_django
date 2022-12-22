# Generated by Django 4.1.3 on 2022-11-30 12:22

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_park', '0002_parkmodel_name'),
        ('cars', '0007_remove_carmodel_age_remove_carmodel_body_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='age',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='auto_park',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='auto_park.parkmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='body_type',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='engine_volume',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='seats',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='carmodel',
            table='car',
        ),
    ]