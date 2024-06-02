# Generated by Django 5.0.6 on 2024-05-30 19:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurements_app', '0004_alter_measurements_hydroponic_system'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='meansurements', to=settings.AUTH_USER_MODEL),
        ),
    ]
