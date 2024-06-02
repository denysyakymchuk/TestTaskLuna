# Generated by Django 5.0.6 on 2024-05-29 18:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydroponic_system_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sensor',
            name='ph',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='tds',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='temperature',
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ph', models.FloatField()),
                ('temperature', models.FloatField()),
                ('tds', models.FloatField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hydroponic_system_app.sensor')),
            ],
        ),
    ]
