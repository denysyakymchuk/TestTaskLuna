from rest_framework import filters as drf_filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from hydroponic_system_app.models import HydroponicSystem
from sensor_app.models import Sensor
from .filters import SensorFilter
from .serializers import SensorWithoutRelationSerializer


class SensorViewSet(viewsets.ModelViewSet):
    """
    API endpoints for sensors.
    """
    queryset = Sensor.objects.all() # Define the queryset attribute
    serializer_class = SensorWithoutRelationSerializer

    filterset_class = SensorFilter
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    ordering_fields = ['sensor_name', 'id', 'time_create', 'time_update']

    def get_queryset(self):
        """
        Get sensors from the database according to the id of the user
        """
        return Sensor.objects.filter(hydroponic_system__owner=self.request.user)

    def perform_create(self, serializer):
        """
        Save new sensor to database
        """
        try:
            HydroponicSystem.objects.filter(id=self.request.data.get('hydroponic_system'), owner=self.request.user)
        except HydroponicSystem.DoesNotExist:
            raise ValidationError("Hydroponic system does not exist or does not belong to the user.")

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

