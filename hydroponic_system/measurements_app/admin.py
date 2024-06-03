from django.contrib import admin

from measurements_app.models import Measurements


@admin.register(Measurements)
class CustomMeasurementAdmin(admin.ModelAdmin):
    list_display = ("hydroponic_system", "owner", "sensor", "ph", "temperature", "tds", "time_create", "time_update")
