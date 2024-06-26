from django_filters import rest_framework as filters
from .models import Measurements


# Define a FilterSet class for HydroponicSystem
class MeasurementsFilter(filters.FilterSet):
    # Define a filter fields
    time_start = filters.DateTimeFilter(field_name='time_create', lookup_expr='gte')
    time_end = filters.DateTimeFilter(field_name='time_create', lookup_expr='lte')

    ph_start = filters.NumberFilter(field_name='ph', lookup_expr='gte')
    ph_end = filters.NumberFilter(field_name='ph', lookup_expr='lte')

    temp_start = filters.NumberFilter(field_name='temperature', lookup_expr='gte')
    temp_end = filters.NumberFilter(field_name='temperature', lookup_expr='lte')

    tds_start = filters.NumberFilter(field_name='tds', lookup_expr='gte')
    tds_end = filters.NumberFilter(field_name='tds', lookup_expr='lte')

    id_start = filters.NumberFilter(field_name='id', lookup_expr='gte')
    id_end = filters.NumberFilter(field_name='id', lookup_expr='lte')

    # Metaclass to provide metadata to the FilterSet
    class Meta:
        model = Measurements
        # Specify the fields on which filtering can be applied
        fields = ['id', 'ph', 'temperature', 'hydroponic_system', 'tds', 'time_create', 'time_update']
