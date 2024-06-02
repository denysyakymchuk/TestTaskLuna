from rest_framework import serializers

from measurements_app.serializers import MeasurementsSerializer
from .models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    """
    Sensor Serializer converting complex data types into Python data types
    """
    measurements = MeasurementsSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class SensorWithoutRelationSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()

    class Meta:
        model = Sensor
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
