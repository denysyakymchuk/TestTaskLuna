# Generated by Django 5.0.6 on 2024-05-30 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_app', '0002_alter_sensor_hydroponic_system'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sensor',
            old_name='name',
            new_name='sensor_name',
        ),
    ]