# Generated by Django 4.1.3 on 2022-12-05 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usermodel_auto_park_alter_usermodel_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='auto_park',
        ),
    ]