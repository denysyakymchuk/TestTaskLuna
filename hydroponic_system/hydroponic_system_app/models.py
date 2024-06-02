from django.contrib.auth.models import User
from django.db import models


class HydroponicSystem(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hydroponic_system')
    hydroponic_system_name = models.CharField(max_length=50)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.hydroponic_system_name}'
