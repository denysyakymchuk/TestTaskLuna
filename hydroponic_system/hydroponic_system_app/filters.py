from django_filters import rest_framework as filters

from hydroponic_system_app.models import HydroponicSystem


# Define a FilterSet class for HydroponicSystem
class HydroponicSystemFilter(filters.FilterSet):
    # Define a filter for start time and end time
    time_start = filters.DateTimeFilter(field_name='time_create', lookup_expr='gte')
    time_end = filters.DateTimeFilter(field_name='time_create', lookup_expr='lte')

    # Metaclass to provide metadata to the FilterSet
    class Meta:
        model = HydroponicSystem
        # Specify the fields on which filtering can be applied
        fields = ['id', 'hydroponic_system_name', 'owner', 'time_create', 'time_update']
