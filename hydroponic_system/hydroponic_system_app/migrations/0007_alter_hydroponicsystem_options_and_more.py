# Generated by Django 5.0.6 on 2024-05-30 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hydroponic_system_app', '0006_delete_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hydroponicsystem',
            options={'ordering': ['hydroponic_system_name']},
        ),
        migrations.RenameField(
            model_name='hydroponicsystem',
            old_name='name',
            new_name='hydroponic_system_name',
        ),
    ]
