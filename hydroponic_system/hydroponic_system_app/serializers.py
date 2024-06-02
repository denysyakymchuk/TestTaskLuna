from rest_framework import serializers

from sensor_app.serializers import SensorWithoutRelationSerializer, SensorSerializer
from .models import HydroponicSystem


class HydroponicSystemSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    sensor = SensorWithoutRelationSerializer(many=True, read_only=True)

    class Meta:
        model = HydroponicSystem
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'owner')