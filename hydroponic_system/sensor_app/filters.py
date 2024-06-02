from django_filters import rest_framework as filters

from sensor_app.models import Sensor


class SensorFilter(filters.FilterSet):
    time_start = filters.DateTimeFilter(field_name='time_create', lookup_expr='gte')
    time_end = filters.DateTimeFilter(field_name='time_create', lookup_expr='lte')

    class Meta:
        model = Sensor
        fields = ['id', 'sensor_name', 'time_create', 'time_update']
