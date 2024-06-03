from django.contrib import admin

from .models import HydroponicSystem


@admin.register(HydroponicSystem)
class CustomHydroponicSystemAdmin(admin.ModelAdmin):
    list_display = ("hydroponic_system_name", "owner", "time_create", "time_update")
