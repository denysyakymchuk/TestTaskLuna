# Generated by Django 5.0.6 on 2024-05-30 09:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydroponic_system_app', '0003_remove_sensor_hydroponic_system_delete_measurements_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydroponicsystem',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hydroponic_system', to='hydroponic_system_app.owner'),
        ),
    ]