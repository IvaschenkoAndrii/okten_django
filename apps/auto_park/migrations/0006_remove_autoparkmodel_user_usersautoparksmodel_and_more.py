# Generated by Django 4.1.4 on 2022-12-18 09:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auto_park', '0005_autoparkmodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autoparkmodel',
            name='user',
        ),
        migrations.CreateModel(
            name='UsersAutoParksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_park', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_park.autoparkmodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cars_auto_parks',
            },
        ),
        migrations.AddField(
            model_name='autoparkmodel',
            name='user',
            field=models.ManyToManyField(related_name='auto_parks', through='auto_park.UsersAutoParksModel', to=settings.AUTH_USER_MODEL),
        ),
    ]