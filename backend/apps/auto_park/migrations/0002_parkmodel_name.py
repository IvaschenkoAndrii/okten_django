# Generated by Django 4.1.3 on 2022-11-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auto_park', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkmodel',
            name='name',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]