from django.contrib.auth.models import User
from django.db import models


from hydroponic_system_app.models import HydroponicSystem
from sensor_app.models import Sensor


class Measurements(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    hydroponic_system = models.ForeignKey(HydroponicSystem, on_delete=models.CASCADE, related_name='measurements', null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meansurements', null=True)
    ph = models.FloatField()
    temperature = models.FloatField()
    tds = models.FloatField()
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hydroponic_system}'

    class Meta:
        verbose_name = "Measurement"
        verbose_name_plural = "Measurements"
        ordering = ("-time_create",)
