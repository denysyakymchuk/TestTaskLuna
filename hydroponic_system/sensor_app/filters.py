from django_filters import rest_framework as filters

from sensor_app.models import Sensor


# Define a FilterSet class for HydroponicSystem
class SensorFilter(filters.FilterSet):
    # Define a filter fields
    time_start = filters.DateTimeFilter(field_name='time_create', lookup_expr='gte')
    time_end = filters.DateTimeFilter(field_name='time_create', lookup_expr='lte')

    # Metaclass to provide metadata to the FilterSet
    class Meta:
        model = Sensor
        # Specify the fields on which filtering can be applied
        fields = ['id', 'sensor_name', 'time_create', 'time_update']
