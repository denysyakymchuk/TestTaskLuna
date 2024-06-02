from django_filters import rest_framework as filters

from hydroponic_system_app.models import HydroponicSystem


class HydroponicSystemFilter(filters.FilterSet):
    time_start = filters.DateTimeFilter(field_name='time_create', lookup_expr='gte')
    time_end = filters.DateTimeFilter(field_name='time_create', lookup_expr='lte')

    class Meta:
        model = HydroponicSystem
        fields = ['id', 'hydroponic_system_name', 'owner', 'time_create', 'time_update']
