# Generated by Django 5.0.6 on 2024-05-29 23:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hydroponic_system_app', '0003_remove_sensor_hydroponic_system_delete_measurements_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('hydroponic_system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hydroponic_system_app.hydroponicsystem')),
            ],
        ),
    ]
