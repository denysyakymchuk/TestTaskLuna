from rest_framework import serializers

from measurements_app.models import Measurements


class MeasurementsSerializer(serializers.ModelSerializer):
    sensor = serializers.StringRelatedField()
    owner = serializers.StringRelatedField()
    hydroponic_system = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Measurements
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at', 'owner')
