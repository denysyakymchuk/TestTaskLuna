from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters as drf_filters, permissions, status
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from sensor_app.models import Sensor
from .models import Measurements
from .serializers import MeasurementsSerializer
from .filters import MeasurementsFilter


class MeasurementsViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Measurements.
    """
    queryset = Measurements.objects.all() # Define the queryset attribute
    serializer_class = MeasurementsSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_class = MeasurementsFilter
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    ordering_fields = ['name', 'id', 'ph', 'temperature', 'tds', 'time_create', 'time_update']

    def get_queryset(self):
        """
        Get hydroponic systems from database according  id of user
        """
        return Measurements.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """
        Save new measurement system to database
        """
        user = self.request.user

        # Check if the sensor exists and belongs to the user
        try:
            sensor = Sensor.objects.get(id=self.request.data.get('sensor'), hydroponic_system__owner=user)
        except Sensor.DoesNotExist:
            raise ValidationError("Sensor does not exist or does not belong to the user.")

        if serializer.is_valid(raise_exception=True):
            # Save the measurement with the associated sensor and hydroponic system
            serializer.save(sensor=sensor, owner=user, hydroponic_system=sensor.hydroponic_system)
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response({}, status.HTTP_400_BAD_REQUEST)

