from rest_framework import filters as drf_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from measurements_app.models import Measurements
from measurements_app.serializers import MeasurementsSerializer
from .filters import HydroponicSystemFilter
from .serializers import HydroponicSystemSerializer
from .models import HydroponicSystem


class HydroponicSystemViewSet(viewsets.ModelViewSet):
    """
    API endpoints for Hydroponic Systems.
    """
    queryset = HydroponicSystem.objects.all() # Define the queryset attribute
    serializer_class = HydroponicSystemSerializer
    permission_classes = [permissions.IsAuthenticated]

    filterset_class = HydroponicSystemFilter
    filter_backends = [DjangoFilterBackend, drf_filters.SearchFilter, drf_filters.OrderingFilter]
    ordering_fields = ['hydroponic_system_name', 'id', 'tds', 'time_create', 'time_update']

    def get_queryset(self):
        """
        Get hydroponic systems from database according  id
        """
        Response(HydroponicSystem.objects.filter(owner=self.request.user), status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        """
        Save new hydroponic system to database
        """
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def detail_hydroponic_system(self, request, pk=None):
        """
        Get hydroponic system detail with last 10 measurements from database according id
        """
        try:
            hydroponic_system = HydroponicSystem.objects.get(pk=pk, owner=self.request.user)
            measurements = Measurements.objects.filter(hydroponic_system=hydroponic_system.id, owner=self.request.user).order_by('-time_create')[:10]

            hydroponic_system_data = self.get_serializer(hydroponic_system).data
            measurements_data = MeasurementsSerializer(measurements, many=True).data

            response_data = {
                'details': hydroponic_system_data,
                'measurements': measurements_data
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except HydroponicSystem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)