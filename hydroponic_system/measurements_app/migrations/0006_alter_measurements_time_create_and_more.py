# Generated by Django 5.0.6 on 2024-05-31 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements_app', '0005_measurements_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='time_create',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='time_update',
            field=models.DateField(auto_now=True),
        ),
    ]
