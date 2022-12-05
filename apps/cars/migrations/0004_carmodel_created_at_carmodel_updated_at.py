# Generated by Django 4.1.3 on 2022-11-30 12:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_carmodel_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='carmodel',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
