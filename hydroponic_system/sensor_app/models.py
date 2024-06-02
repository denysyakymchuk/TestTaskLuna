from django.db import models

from hydroponic_system_app.models import HydroponicSystem


class Sensor(models.Model):
    hydroponic_system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE, related_name='sensor')
    sensor_name = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.sensor_name}'
    