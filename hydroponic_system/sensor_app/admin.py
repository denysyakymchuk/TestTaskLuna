from django.contrib import admin

from sensor_app.models import Sensor


@admin.register(Sensor)
class CustomSensorAdmin(admin.ModelAdmin):
    list_display = ("hydroponic_system", "sensor_name", "time_create", "time_update")