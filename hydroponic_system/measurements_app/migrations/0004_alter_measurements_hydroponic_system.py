# Generated by Django 5.0.6 on 2024-05-30 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hydroponic_system_app', '0007_alter_hydroponicsystem_options_and_more'),
        ('measurements_app', '0003_measurements_hydroponic_system'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='hydroponic_system',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='measurements', to='hydroponic_system_app.hydroponicsystem'),
        ),
    ]